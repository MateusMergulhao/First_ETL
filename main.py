from extract import extract_data
from transform import transform_data
from load import load_data
from config import MONGO_URI, CSV_FILE

def run_etl():

    # Extract
    data = extract_data(CSV_FILE)

    # Transform
    data = transform_data(data)

    # Load
    load_data(data, MONGO_URI)


if __name__ == "__main__":
    run_etl()