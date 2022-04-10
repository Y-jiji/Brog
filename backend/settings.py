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
    "host:port": "database.rainspace.cn:3306",
    "database": "brog",
    "username": "brog",
    "password": "Brog2022",
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
FILE_PATH_IMG = path.join(path.dirname(__file__), "image")

## 邮箱验证码
SENDER_ADDRESS = '799066947@qq.com'
SENDER_PASS = 'fscoaectlhobbefg'


HOST_ = "127.0.0.1"
PORT_ = "8000"