from pathlib import Path

import pandas as pd
from config import DATASET_DIR
from utils.logging import get_logger

logger = get_logger(__name__)

DATA_FILES = ["movies", "links", "ratings", "tags"]


def extract() -> dict[str, pd.DataFrame]:
    data: dict[str, pd.DataFrame] = {}
    dataset_path = Path(DATASET_DIR)

    for name in DATA_FILES:
        file_path = dataset_path / f"{name}.csv"
        try:
            df = pd.read_csv(file_path)
            data[name] = df
            logger.info("Loaded %s.csv with %d rows", name, len(df))
        except FileNotFoundError:
            logger.error("Missing %s", file_path)
        except Exception as e:
            logger.error("Failed to load %s.csv: %s", name, e)

    if "movies" not in data:
        raise FileNotFoundError(
            f"movies.csv is required under {dataset_path}. "
            "Add MovieLens CSVs to the dataset folder."
        )

    logger.info("Data extraction complete (%d tables)", len(data))
    return data
