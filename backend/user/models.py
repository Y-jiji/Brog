from _ext.sqlalchemy import Boolean, Column, Integer, String, engine
from database import Base


class Field(Base):
    __tablename__ = "field"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True)
