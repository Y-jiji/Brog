from datetime import datetime
from re import T
from _ext.sqlalchemy import *
from sqlalchemy.sql import func

class SqlUser(Base):
    __tablename__ = "user_auth"
    id = Column(String(10), primary_key=True, index=True)
    name = Column(String(30), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    pwd = Column(String(100))
    token = Column(String(20))
    is_active = Column(Boolean, default=True)

class Captcha(Base):
    __tablename__ = "captcha"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), index = True)
    captcha = Column(String(10), )
    time = Column(DateTime(timezone=True), server_default=func.now())