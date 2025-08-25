import os
from sqlalchemy import create_engine, text
DB_USER = os.getenv("POSTGRES_USER", "lijoa")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "lijoa")
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "lijoa")
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
def db_ok() -> bool:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))  
    return True
