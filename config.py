import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
CSV_FILE = os.getenv("CSV_FILE")