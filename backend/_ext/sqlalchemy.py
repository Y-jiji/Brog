__all__ = [
    "db",
    "engine",
    "SessionLocal",
    "Base",
    "Column",
    "String",
    "Integer",
    "Boolean",
    "DateTime"
]

from settings import SQLALCHEMY_CONFIG as CONFIG
from sqlalchemy import create_engine, Column, String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    CONFIG["url"],
    connect_args=CONFIG["connect_args"],
    echo=CONFIG["echo"]
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

db = SessionLocal()
