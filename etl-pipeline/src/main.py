from etl.extract import extract
from etl.load import load
from etl.transform import transform
from utils.logging import get_logger

logger = get_logger(__name__)


def process() -> None:
    extracted = extract()
    documents = transform(extracted)
    load(documents)


if __name__ == "__main__":
    try:
        process()
    except Exception as e:
        logger.error("ETL pipeline failed: %s", e)
        raise
