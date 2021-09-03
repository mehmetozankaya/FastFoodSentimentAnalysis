from dotenv import load_dotenv
from pathlib import Path  # python3 only
import os
from pymongo import MongoClient

# set path to env file
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


class Mongo:
    """Create MongoDB Connections from .env file"""

    # Load in enviornemnt variables
    client = MongoClient(os.getenv('CONN_STRING'),tls=True,tlsAllowInvalidCertificates=True)
    db = client.get_database(os.getenv('DB_NAME'))
    originalCol = db[os.getenv('Original_COL')]
    kfcCol = db[os.getenv('KFC_WC')]
    subwayCol = db[os.getenv('SUBWAY_COL')]
    mcdCol = db[os.getenv('MCD_WC')]
    dominosCol = db[os.getenv('DOMINOS_WC')]
    timCol = db[os.getenv('TIM_WC')]
