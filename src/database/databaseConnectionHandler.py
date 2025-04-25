# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
from pydantic import Field
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#TODO: will make these classes later, using direct variables for now for DB connection
# class DatabaseConnectionHandler(BaseSettings):
#     """
#         Config class that defines database settings
#     """
#     db_name: str = os.getenv("DB_NAME")
#     db_user: str = os.getenv("DB_USER")
#     db_host: str = os.getenv("DB_HOST")
#     db_port: int = os.getenv("DB_PORT")
#     db_password: str = os.getenv("DB_PASSWORD")
#     db_pool_size: int = 5
#     class Config:
#         env_file = ".env"
#         extra = "ignore"
#

db_name: str = os.getenv("DB_NAME")
db_user: str = os.getenv("DB_USER")
db_host: str = os.getenv("DB_HOST")
db_port: int | str = os.getenv("DB_PORT")
db_password: str = os.getenv("DB_PASSWORD")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=5,
    pool_pre_ping=True,
    pool_recycle=3600
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()