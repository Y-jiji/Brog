from os import path

CORS_CONFIG = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"]
}

THIS_DIR = path.dirname(__file__)

FILE_PATH = path.join(THIS_DIR, "uploadedFile")

STATIC_PATH = path.join(THIS_DIR, "static")