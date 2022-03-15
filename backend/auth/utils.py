# 基于本文件夹的依赖项
import email
from time import time

from sqlalchemy import false
from auth.models import SqlUser, Captcha
from auth.schemas import UserAuth


# 基于父文件夹的依赖项
from _ext.sqlalchemy import *
from _ext.security import get_password_hash, getRandStr, getRandDigStr
from settings import * 

# 外部依赖项
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib, random, datetime

# 基于全局的依赖项
from fastapi import HTTPException, status
from sqlalchemy.sql.expression import or_

async def tryUserCreate(sqlUser: SqlUser):
    try:
        print(len(sqlUser.pwd))
        db.add(sqlUser)
        db.commit()
        db.refresh(sqlUser)
        return sqlUser
    except:
        db.rollback()
        return None


async def userCreate(user: UserAuth):
    sqlUser = SqlUser(
        id=getRandStr(10),
        name=user.name,
        email=user.email,
        pwd=user.pwd,
        token=getRandStr(20)
    )
    for cnt in range(20):
        ok = await tryUserCreate(sqlUser)
        if ok:
            return ok
        sqlUser.id = getRandStr(10)
    db
    return None


async def userAlready(user: UserAuth):
    sqlUser: SqlUser = db.query(SqlUser).filter_by(name=user.name).first()
    return True if sqlUser else False


async def userVerify(user: UserAuth):
    try:
        if user.name:
            sqlUserSet = db.query(SqlUser).filter_by(name = user.name).filter_by(pwd = user.pwd)
        elif user.id:
            sqlUserSet = db.query(SqlUser).filter_by(id = user.id).filter_by(token = user.token)
        # 如果用户登录信息是错的, 那么这个集合是空集, 不会干扰正常用户
        # 同时因为name和id的唯一性, 这个集合至多只有一个元素, 不存在修改多个用户的问题
        sqlUserSet.update({SqlUser.token: getRandStr(20)})
        sqlUser = sqlUserSet.first()
        # obj = db.query(SqlUser).filter_by(email = user.email)
        db.commit()
        assert sqlUser
    except:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="user is None"
        )
    return sqlUser

async def user_token(name, token):
    obj = db.query(SqlUser).filter_by(name = name).first()
    print(obj.token)
    print(token)
    return obj.token == token


async def changeToken(user: UserAuth):
    try:
        sqlUserSet = db.query(SqlUser).filter(
            or_(SqlUser.name == user.name,
                SqlUser.id == user.id,
                SqlUser.token == user.token))
        assert sqlUserSet.update({SqlUser.token: getRandStr(20)}).first()
    except:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="user is None"
        )

async def checkCaptcha(email: str):
    obj = db.query(Captcha).filter(Captcha.email == email).first()
    if (not obj):
        return True
    time_tmp = obj.time
    time_now = datetime.datetime.now()
    duration = time_now - time_tmp
    if (duration.seconds > 120):
        return True
    else:
        return False

async def insertCaptcha(email: str, captcha: str):
    db_tmp_captcha_obj = db.query(Captcha).filter(Captcha.email == email).first()
    if (db_tmp_captcha_obj):
        db_tmp_captcha_obj.time = datetime.datetime.now()
    else:
        db_tmp_captcha_obj = Captcha(email=email, captcha=captcha)
        # print(db_tmp_captcha_obj)
        db.add(db_tmp_captcha_obj)
    db.commit()
    db.refresh(db_tmp_captcha_obj)
    return db_tmp_captcha_obj

async def queryCaptcha(email: str):
    return db.query(Captcha).filter(Captcha.email == email).order_by(Captcha.id.desc()).first()

async def sendCaptcha(email: str):
    captcha = getRandDigStr(6)
    msg = MIMEText('验证码为：' + str(captcha), 'plain', 'utf-8')
    msg['From'] = formataddr(["From Brog", SENDER_ADDRESS])  # 发件人昵称， 发件人邮箱
    msg['To'] = formataddr(["尊贵的用户", email])  # 收件人昵称
    msg['Subject'] = "Brog验证码"  # 主题

    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # SMTP服务器
    server.login(SENDER_ADDRESS, SENDER_PASS)  # 授权码
    server.sendmail(SENDER_ADDRESS, [email, ], msg.as_string())  
    server.quit()  # 关闭连接
    try:
        obj = await insertCaptcha(email, captcha)
        # print(obj)
    except:
        print("插入记录失败")
        
async def verifyCaptcha_(email: str, captcha: str):
    captcha_obj = await queryCaptcha(email)
    return ((captcha_obj != None) and (captcha_obj.captcha == captcha))
    
async def pwdUpdate(email: str, pwd: str):
    db_tmp_user_obj = db.query(SqlUser).filter(SqlUser.email==email)
    db_tmp_user_obj.pwd = pwd
    db.commit()
     
async def insert_user(email: str, pwd: str, name: str):
    print(email)
    db_tmp_user_obj = db.query(SqlUser).filter(SqlUser.email==email).first()
    print(db_tmp_user_obj)
    # if db_tmp_user_obj != {}:
    #     return False
    db_tmp_user_obj = SqlUser(email = email, name = name, pwd = get_password_hash(pwd))
    print(999)
    print(db_tmp_user_obj)
    # db.add(db_tmp_user_obj)
    # db.commit()
    # db.refresh()
    return True