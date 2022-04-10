__all__ = [
    'auth',
]

# 全局依赖
from sympy import re
from settings import SENDER_ADDRESS, SENDER_PASS

# 基于本文件夹的依赖项
from .utils import *
from .schemas import *  # 前端传输过来的数据类型
from .models import *

# 外部依赖项
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, Request, Response
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib, random
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

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
async def register(user: UserAuth, captcha: str, req: Request, resp: Response):
    if await userAlready(user):
        return {"status": "failure", "msg": "nameCrash"}
    if not await verifyCaptcha_(user.email, captcha):
        return {"status": "failure", "msg": "captcha error"}
    sqlUser = await userCreate(user)
    if not sqlUser:
        return {"status": "failure", "msg": "idCrashTooManyTimes"}
    setAllCookies(resp, sqlUser)
    return {"status": "success"}


@auth.post("/login")
async def login(user: UserAuth, req: Request, resp: Response):
    sqlUser: SqlUser = await userVerify(user=user)
    if not sqlUser:
        return {"status": "failure"}
    setAllCookies(resp, sqlUser)
    print(sqlUser.token)
    return {"status": "success"}


def login_required(func):
    async def inner(user: UserAuth, req: Request):
        if (not await user_token(user.name, req.cookies["token"])):
            print(2)
            return {"status": "failure", "msg": "no token"}
        print(1)
        await func(user, req, **kwargs)

    return inner


@auth.post("/logout")
async def logout(req: Request, resp: Response):
    for x in ["id", "token", "hashed_token"]:
        resp.delete_cookie(x, path="brog/auth")
    return {"status": "success"}


@auth.post('/test')
async def test(user: UserAuth, req: Request, kk: str):
    print(999)


@auth.post("/read-token")
async def readToken(name: str, req: Request, resp: Response):
    print(req.cookies)
    print(await user_token(name, "11"))
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
        return {'status': 'failure', 'msg': "发送验证码太频繁"}
    try:
        await sendCaptcha(email=email)
        return {'status': 'success', 'msg': "验证码发送成功"}
    except Exception:
        return {'status': 'failure', 'msg': "验证码发送失败"}


@auth.get("/verify_captcha")
async def verifyCaptcha(req: Request, email: str, captcha: str, resp: Response):
    return {'status': 'success', 'jud': await verifyCaptcha_(email, captcha)}


@auth.get("/forget")
async def pwdForget(req: Request, email: str, pwd: str, resp: Response):
    ## 前端先邮箱验证
    ## 这边处理直接更新?
    ## 密码格式检测
    try:
        await pwdUpdate(email, pwd);
        return {'status': 'success', 'msg': "修改密码成功"}
    except Exception as e:
        print(e)
        return {"status": 'failure', 'msg': '修改密码失败'}


# from _ext.security import verify_password, create_access_token
# from .models import SqlUser
# @auth.post("/my_login", summary="登录")
# async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
#     if user := await SqlUser.get(username = form_data.username):
#         if (verify_password(form_data.password, user.password)):
#             return {"access_token": create_access_token({"email": user.email}), "token_type":"bearer"}
#         return {"status": "failure", "msg" : ""}

# @auth.post("/my_register", summary="注册")
# async def user_register(user:UserAuth):
#     jud = await insert_user(**user.dict())
#     if jud:
#         return {"status": "success", "msg":"注册成功"}
#     else:
#         return {"status": "failure", "msg":"邮箱已被注册"}


@auth.get("/msg")
async def test_msg(req: Request, resp: Response):
    return {"message": "跨域？"}


@auth.get("/profile")
async def getUserProfile(req: Request):
    if (req.cookies["token"]):
        try:
            obj_tmp = await queryProfile(token=req.cookies["token"])
            return {'status': 'success', "profile_obj": obj_tmp}

        except Exception as e:
            print(e)
            return {'status': 'failure', "msg": "查询失败"}
    else:
        return {'status': 'failure', "msg": "请先登录"}
