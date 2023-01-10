from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

ENGINE = create_engine(os.getenv("CONNECTION"))
