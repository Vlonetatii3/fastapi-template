from pydantic import BaseSettings

#Oracle
class Settings(BaseSettings):
    ORACLE_USER: str
    ORACLE_PASSWORD: str
    ORACLE_HOST: str
    ORACLE_PORT: int = 1521
    ORACLE_SERVICE: str

    class Config:
        env_file = ".env"

settings = Settings()

#PostgreSQL
class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str

    class Config:
        env_file = ".env"
