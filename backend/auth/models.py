from _ext._sqlalchemy import *
from _ext._neo4j import CypherEngine
from _ext.ext_settings import NEO4J_CONFIG

class SqlUser(Base):
    """
    Sql中存储的用户信息, 主要是关于登录注册的
    """
    __tablename__ = "user_auth"
    id = Column(String(10), primary_key=True, index=True)
    name = Column(String(30), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    pwd = Column(String(100))
    token = Column(String(20))
    is_active = Column(Boolean, default=True)

class NoSqlUser:
    def __init__(self):
        self.driver = CypherEngine()