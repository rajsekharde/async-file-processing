from sqlmodel import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv("POSRGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"


engine = create_engine(
    DATABASE_URL,
    echo=False
)