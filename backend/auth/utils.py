# 基于本文件夹的依赖项
from auth.models import SqlUser
from auth.schemas import UserAuth
from auth.coding import pwdCtxt


# 基于父文件夹的依赖项
from _ext.sqlalchemy import *


# 基于全局的依赖项
from fastapi import HTTPException, status
from sqlalchemy.sql.expression import or_
from random import choices
from string import ascii_letters, digits
from typing import Optional


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
    def getRandStr(length):
        return "".join(choices(ascii_letters + digits, k=length))
    sqlUser = SqlUser(
        id=getRandStr(10),
        name=user.name,
        pwd=user.pwd,
        token=getRandStr(20)
    )
    for cnt in range(20):
        ok = await tryUserCreate(sqlUser)
        if ok:
            return ok
        sqlUser.id = getRandStr(10)
    return None


async def userAlready(user: UserAuth):
    sqlUser: SqlUser = db.query(SqlUser).filter_by(name=user.name).first()
    return True if sqlUser else False


async def userVerify(user: UserAuth):
    def getRandToken():
        return "".join(choices(ascii_letters + digits, k=20))
    try:
        sqlUserSet = db.query(SqlUser).filter(
            or_(SqlUser.name == user.name, SqlUser.id == user.id),
            or_(SqlUser.pwd == user.pwd, SqlUser.token == user.token)
        )
        # 如果用户登录信息是错的, 那么这个集合是空集, 不会干扰正常用户
        sqlUserSet.update(token=getRandToken())
        sqlUserSet.first()
    except:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="user is None"
        )
    return sqlUserSet.first()
