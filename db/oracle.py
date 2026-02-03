from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

DATABASE_URL = (
    f"oracle+oracledb://{settings.ORACLE_USER}:"
    f"{settings.ORACLE_PASSWORD}@"
    f"{settings.ORACLE_HOST}:"
    f"{settings.ORACLE_PORT}/"
    f"?service_name={settings.ORACLE_SERVICE}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_oracle_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
