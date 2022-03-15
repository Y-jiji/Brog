# from pydantic import BaseModel

from _ext.sqlalchemy import *

# from database import Base


class Note(Base):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True, index=True)
    note_name = Column(String(255))
    content = Column(LONGTEXT)
    status = Column(Boolean, default=False)
    is_delete = Column(Boolean, default=False)