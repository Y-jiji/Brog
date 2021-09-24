from os import path

CORS_CONFIG = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"]
}


SQLALCHEMY_CONFIG = {
    "py_engine": "pymysql",
    "real_engine": "mysql",
    "host:port": "localhost:3306",
    "database": "brog_db",
    "username": "root",
    "password": "root",
    "connect_args": {},
    "echo": True
}


def get_SQLALCHEMY_CONFIG_URL(x): return "%s+%s://%s:%s@%s/%s" % (
    x["real_engine"], x["py_engine"],
    x["username"], x["password"],
    x["host:port"], x["database"]
)


SQLALCHEMY_CONFIG["url"] = get_SQLALCHEMY_CONFIG_URL(SQLALCHEMY_CONFIG)


FILE_PATH = path.join(path.dirname(__file__), "uploadedFile")
