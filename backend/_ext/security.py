__all__ = [
    'secureCtx',
    'getRandStr'
]

from passlib.hash import bigcrypt
from passlib.context import CryptContext
from random import choices
from string import ascii_letters, digits


def getRandStr(length):
    return "".join(choices(ascii_letters + digits, k=length))


secureCtx: CryptContext = bigcrypt(
    salt="ab")

if __name__ == "__main__":
    print(secureCtx.hash("123456"))
