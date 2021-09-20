# Forewords

网络安全部分基本都是自己实现的, 目前看来基本上没有什么坑. 


# Dependencies

## Web
```shell

pip install uvicorn fastapi 

```

## Sql
```shell

pip install sqlalchemy pymysql

```


# Run

Double click `app.py` in this folder will start this script(in windows). 

Or `python app.py` in shell, after change directory to this folder. 

# Configuration

Everything concerning cofiguration is in settings.py. 

## Configure CORS

what the key suggests literally is its real meaning.  

```python

CORS_CONFIG = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"]
}

```

## Configure Database

Fit them your local conditions, e.g.: usernames and roots are usually different from this. 

```python

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

```

# Manage Database

Double click `manager.py` in this folder will start this script(in windows). 

Or `python manager.py` in shell, after change directory to this folder. 

if you want to drop all tables, just type `drop all tables`

if you want to create all tables, just type `create all tables`


# Read Auto Document Prepared By SwaggerUI

## \<path\>/docs
  
Open \<path\>/docs to read information about it, in which \<path\> can be: 
  - '/file'
  - '/auth'
  - '/' (which means the root)
