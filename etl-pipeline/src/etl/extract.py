from pathlib import Path

import pandas as pd
from utils.logging import get_logger

logger = get_logger(__name__)


def extract():
    CSV_PATH = Path(__file__).parent.parent.parent / "dataset" / "links.csv"

    for chunk in pd.read_csv(CSV_PATH, chunksize=100):
        print(chunk.head())
