# 平级组件可以调用的函数(主要是些装饰器)
# public层级不应该依赖任何一个名为app.py的文件中的任何内容

__all__ = [
    "login_required",
]

# 全局依赖
from typing import Optional
from fastapi import status, HTTPException, Request, Response, WebSocket
from functools import wraps

# 父级依赖
from _ext.security import secureCtx

# 本文件夹依赖
from .schemas import UserAuth
from .utils import changeToken


def login_required(func):
    @wraps(func)
    async def inner(req: Request, resp: Response, *args, **kwargs):
        cookies = req.cookies
        if "token" in cookies and "hashed_token" in cookies and\
                secureCtx.verify(cookies["token"], cookies["hashed_token"]):
            for x in cookies:
                resp.set_cookie(x, cookies[x],
                                expires=10800, path="/brog/auth")
            return await func(req=req, resp=resp, *args, **kwargs)
        if "id" in cookies:
            changeToken(UserAuth(id=cookies['id']))
            for x in ["id", "token", "hashed_token"]:
                resp.delete_cookie(x, path="/brog/auth")
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Bad Token"
        )
    return inner
