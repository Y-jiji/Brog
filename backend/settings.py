CORS_CONFIG = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"]
}

SQLALCHEMY_CONFIG = {
    "database_url": "mysql+pymysql://root:root@localhost:3306/brog_db",
    "connect_args": {},
    "echo": True
}
