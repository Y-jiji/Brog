__all__ = [
    'auth',
]

# 基于本文件夹的依赖项
from .utils import *
from .schemas import *  # 前端传输过来的数据类型
from .models import *

# 外部依赖项
from datetime import datetime, timedelta
from fastapi import FastAPI, Request, Response

# 父级依赖项
from _ext.security import secureCtx

auth = FastAPI()


def setAllCookies(resp: Response, sqlUser):
    resp.set_cookie("id", sqlUser.id, expires=10800)
    resp.set_cookie("token", sqlUser.token, expires=10800)
    resp.set_cookie("hashed_token", secureCtx.hash(
        sqlUser.token), expires=10800)


@auth.post("/register")
async def register(user: UserAuth, req: Request, resp: Response):
    if await userAlready(user):
        return {"status": "failure", "reason": "nameCrash"}
    sqlUser = await userCreate(user)
    if not sqlUser:
        return {"status": "failure", "reason": "idCrashTooManyTimes"}
    setAllCookies(resp, sqlUser)
    return {"status": "success"}


@auth.post("/login")
async def login(user: UserAuth, req: Request, resp: Response):
    sqlUser: SqlUser = await userVerify(user=user)
    if not sqlUser:
        return {"status": "failure"}
    setAllCookies(resp, sqlUser)
    return {"status": "success"}


@auth.post("/logout")
async def logout(req: Request, resp: Response):
    for x in ["id", "token", "hashed_token"]:
        resp.delete_cookie(x, path="brog/auth")
    return {"status": "success"}


@auth.post("/read-token")
async def readToken(req: Request, resp: Response):
    return {
        "status": "success",
        "token": req.cookies["token"],
        "hashed_token": req.cookies["hashed_token"]
    }


@auth.get("/test/fake-login")
async def hardSetCookies(req: Request, resp: Response):
    req.cookies.clear()
    setAllCookies(resp, SqlUser(
        id='test',
        pwd='123456',
        token='123456'
    ))
    return {"status": "success"}
