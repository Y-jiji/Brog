__all__ = [
    'auth',
]

# 基于本文件夹的依赖项
from starlette.requests import Request
from starlette.responses import Response
from auth.utils import *
from auth.schemas import *  # 前端传输过来的数据类型
from auth.coding import *  # 加密算法和密钥
from auth.models import *

# 外部依赖项
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, Request, Response

auth = FastAPI()


@auth.post("/register")
async def register(user: UserAuth, req: Request, resp: Response):
    if await userAlready(user):
        return {"status": "failure", "reason": "nameCrash"}
    sqlUser = await userCreate(user)
    if not sqlUser:
        return {"status": "failure", "reason": "idCrashTooManyTimes"}
    resp.set_cookie("id", sqlUser.id)
    resp.set_cookie("token", sqlUser.token)
    return {"status": "success"}


@auth.post("/login")
async def login(user: UserAuth, req: Request, resp: Response):
    sqlUser = await userVerify(user=user)
    if not sqlUser:
        return {"status": "failure"}
    resp.set_cookie("id", sqlUser.id)
    resp.set_cookie("token", sqlUser.token)
    return {"status": "success"}