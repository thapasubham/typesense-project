from pathlib import Path

import pandas as pd
from utils.logging import get_logger

logger = get_logger(__name__)


def extract():
    files = ["movies", "links", "ratings", "tags"]
    data = {}

    dataset_path = Path("./dataset")

    for file in files:
        file_path = dataset_path / f"{file}.csv"
        try:
            df = pd.read_csv(file_path)
            data[file] = df

            logger.info(f"Loaded {file}.csv with {len(df)} rows")

        except Exception as e:
            logger.error(f"Failed to load {file}.csv: {e}")
    logger.info("Data extraction complete")
    return data
