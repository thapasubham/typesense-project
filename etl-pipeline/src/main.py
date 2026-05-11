from etl.extract import extract
from utils.db import init_db

extract()
init_db()
