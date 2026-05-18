import os
from pathlib import Path

ETL_ROOT = Path(__file__).resolve().parents[1]
DATASET_DIR = ETL_ROOT / "dataset"
PIPELINE_DIR = ETL_ROOT / "pipeline"

TYPESENSE_HOST = os.getenv("TYPESENSE_HOST", "localhost")
TYPESENSE_PORT = os.getenv("TYPESENSE_PORT", "8108")
TYPESENSE_PROTOCOL = os.getenv("TYPESENSE_PROTOCOL", "http")
TYPESENSE_API_KEY = os.getenv("TYPESENSE_API_KEY", "xyz")
TYPESENSE_COLLECTION = os.getenv("TYPESENSE_COLLECTION", "movies")

MOVIES_SCHEMA = {
    "name": TYPESENSE_COLLECTION,
    "fields": [
        {"name": "title", "type": "string"},
        {"name": "genres", "type": "string[]", "facet": True},
        {"name": "tags", "type": "string[]", "facet": True},
        {"name": "average_rating", "type": "float"},
        {"name": "ratings_count", "type": "int32", "facet": True},
    ],
    "default_sorting_field": "ratings_count",
}
