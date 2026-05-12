from etl.extract import extract
from etl.load import load
from etl.transform import transform


def process():
    extracted = extract()
    transformed = transform(extracted)
    load(transformed)


process()
