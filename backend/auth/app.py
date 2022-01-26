__all__ = [
    'auth',
]

# 全局依赖
from settings import SENDER_ADDRESS, SENDER_PASS

# 基于本文件夹的依赖项
from .utils import *
from .schemas import *  # 前端传输过来的数据类型
from .models import *

# 外部依赖项
from datetime import datetime, timedelta
from fastapi import FastAPI, Request, Response
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib, random

# 父级依赖项
from _ext.security import secureCtx

auth = FastAPI()
Base.metadata.create_all(bind=engine)

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
    print(req.cookies)
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

@auth.get("/email_captcha")
async def emailCaptcha(req: Request, email: str, resp: Response):
    jud = await checkCaptcha(email)
    if (not jud):
        return {'status':'failure', 'msg':"发送验证码太频繁"}
    try:
        await sendCaptcha(email=email)
        return {'status':'success', 'msg':"验证码发送成功"}
    except Exception:
        return {'status':'failure', 'msg':"验证码发送失败"}

@auth.get("/verify_captcha")
async def verifyCaptcha(req: Request, email: str, captcha: str, resp: Response):
    return {'status': 'success', 'jud': await verifyCaptcha_(email, captcha)}

@auth.get("/forget")
async def pwdForget(req: Request, email: str, pwd: str, resp: Response):
    ## 前端先邮箱验证
    ## 这边处理直接更新?
    try:
        await pwdUpdate(email,pwd);
        return {'status':'success', 'msg':"修改密码成功"}
    except Exception:
        return {"status":'failure', 'msg':'修改密码失败'}