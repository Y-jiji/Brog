# from pydantic import BaseModel

from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class Pdf_File(Base):
    __tablename__ = "pdf_file"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), unique=True, index=True)
    file_path = Column(String(255), unique=True)
    is_delete = Column(Boolean, default=False)