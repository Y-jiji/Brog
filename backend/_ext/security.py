__all__ = [
    'secureCtx',
    'getRandStr'
]

from typing import Optional
from passlib.hash import bigcrypt
from passlib.context import CryptContext
from random import choices
from string import ascii_letters, digits
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def getRandStr(length):
    return "".join(choices(ascii_letters + digits, k=length))

def getRandDigStr(length):
    return "".join(choices(digits, k=length))

secureCtx: CryptContext = bigcrypt(
    salt="ab")

if __name__ == "__main__":
    print(secureCtx.hash("123456"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
##验证明文密码和哈希密码
def verify_password(plain_password:str, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

##加密
def get_password_hash(password:str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=1)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
