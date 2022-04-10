# from pydantic import BaseModel

from _ext.sqlalchemy import Boolean, Column, Integer, String, engine
from database import Base


class Pdf_File(Base):
    __tablename__ = "pdf_file"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), unique=True, index=True)
    file_path = Column(String(255), unique=True)
    cover_path = Column(String(255), unique=True)
    is_delete = Column(Boolean, default=False)

class Personal_File(Base):
    __tablename__ = "personal_file"
    id = Column(Integer, primary_key=True, index=True)
    bid = Column(Integer)
    username = Column(String(255))
    page = Column(Integer)

