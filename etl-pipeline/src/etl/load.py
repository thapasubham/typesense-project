import json
from pathlib import Path
from typing import Any

import typesense
from config import (
    MOVIES_SCHEMA,
    PIPELINE_DIR,
    TYPESENSE_API_KEY,
    TYPESENSE_COLLECTION,
    TYPESENSE_HOST,
    TYPESENSE_PORT,
    TYPESENSE_PROTOCOL,
)
from etl.transform import documents_to_jsonl
from utils.logging import get_logger

logger = get_logger(__name__)


def _typesense_client() -> typesense.Client:
    return typesense.Client(
        {
            "nodes": [
                {
                    "host": TYPESENSE_HOST,
                    "port": int(TYPESENSE_PORT),
                    "protocol": TYPESENSE_PROTOCOL,
                }
            ],
            "api_key": TYPESENSE_API_KEY,
            "connection_timeout_seconds": 10,
        }
    )


def _ensure_collection(client: typesense.Client) -> None:
    try:
        client.collections[TYPESENSE_COLLECTION].retrieve()
        logger.info("Collection '%s' already exists", TYPESENSE_COLLECTION)
    except typesense.exceptions.ObjectNotFound:
        client.collections.create(MOVIES_SCHEMA)
        logger.info("Created collection '%s'", TYPESENSE_COLLECTION)


def _parse_import_result(result: str | list[dict[str, Any]]) -> list[dict[str, Any]]:
    """import_ returns a raw JSONL string for str input, or parsed dicts for list input."""
    if isinstance(result, list):
        return result
    return [json.loads(line) for line in result.strip().split("\n") if line.strip()]


def _write_jsonl(documents: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    jsonl = documents_to_jsonl(documents)
    path.write_text(jsonl + "\n", encoding="utf-8")
    logger.info("Wrote %d documents to %s", len(documents), path)


def load(documents: list[dict]) -> None:
    if not documents:
        raise ValueError("No documents to load")

    jsonl_path = Path(PIPELINE_DIR) / f"{TYPESENSE_COLLECTION}.jsonl"
    _write_jsonl(documents, jsonl_path)

    client = _typesense_client()
    _ensure_collection(client)

    logger.info("Importing into Typesense collection '%s'...", TYPESENSE_COLLECTION)
    raw_result = client.collections[TYPESENSE_COLLECTION].documents.import_(
        documents,
        {"action": "upsert"},
    )
    import_lines = _parse_import_result(raw_result)

    failed = [line for line in import_lines if not line.get("success")]
    if failed:
        logger.error("Import had %d failures (first: %s)", len(failed), failed[0])
        raise RuntimeError(f"Typesense import failed for {len(failed)} documents")

    logger.info("Loaded %d documents into Typesense", len(documents))
