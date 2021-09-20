# 加密模块
__all__ = [
    'pwdCtxt',
]

from jose import jwt, JWTError
from passlib.context import CryptContext as Ctxt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

ALGORITHMS = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwdCtxt = Ctxt(schemes=['sha256_crypt'])

if __name__ == '__main__':
    hashCode = pwdCtxt.hash("123456")
    print(hashCode)
    if pwdCtxt.verify("123456", hashCode):
        print("OK")
    else:
        print("Bad")
