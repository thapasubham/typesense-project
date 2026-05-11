import csv
import os

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from utils.logging import get_logger

logger = get_logger(__name__)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "typesense_db")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "typesense-password")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def get_engine() -> Engine:
    logger.info("Creating DB engine: %s:%s/%s", DB_HOST, DB_PORT, DB_NAME)
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    return engine


def check_connection():
    try:
        with get_engine().connect() as conn:
            conn.execute(text("SELECT 1"))
            logger.info("Connected to the database")
    except SQLAlchemyError as e:
        logger.fatal(f"Failed to conect with the db: {e}")


def init_db():
    with open("./dataset/movies.csv", "r", newline="") as f:
        csv_data = csv.reader(f)
        header = next(csv_data)
        print(header)
