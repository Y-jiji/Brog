# 平级组件可以调用的函数(主要是些装饰器)
# public层级不应该依赖任何一个app.py中的任何内容

__all__ = [
    "login_required",
]

from auth.schemas import UserAuth
from typing import Dict

from fastapi import status, HTTPException, Request
from functools import wraps
from auth.utils import userVerify


def login_required(func):
    @wraps(func)
    async def inner(req: Request, *args, **kwargs):
        cookies = req.cookies
        if userVerify(UserAuth(
            id=cookies["id"],
            token=cookies["token"]
        )):
            return await func(req=req, *args, **kwargs)
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Bad Token"
        )
    return inner
