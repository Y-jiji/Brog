# 基于本文件夹的依赖项
from auth.models import SqlUser
from auth.schemas import UserAuth


# 基于父文件夹的依赖项
from _ext.sqlalchemy import *
from _ext.security import getRandStr


# 基于全局的依赖项
from fastapi import HTTPException, status
from sqlalchemy.sql.expression import or_

async def tryUserCreate(sqlUser: SqlUser):
    """
    进行一次将用户注册如数据库的尝试, sqlUser为SqlAlchemy模型对象
    """
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
    """
    把用户加入数据库, user为Pydantic模型对象
    """
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
    """
    查询数据库中是否已有用户, user为Pydantic模型对象
    """
    sqlUser: SqlUser = db.query(SqlUser).filter_by(name=user.name).first()
    return True if sqlUser else False


async def userVerify(user: UserAuth):
    """
    查询数据库用户信息是否正确, user为Pydantic模型对象
    """
    try:
        if user.name:
            sqlUserSet = db.query(SqlUser).filter_by(name = user.name).filter_by(pwd = user.pwd)
        elif user.id:
            sqlUserSet = db.query(SqlUser).filter_by(id = user.id).filter_by(token = user.token)
        # 如果用户登录信息是错的, 那么这个集合是空集, 不会干扰正常用户
        # 同时因为name和id的唯一性, 这个集合至多只有一个元素, 不存在修改多个用户的问题
        sqlUserSet.update({SqlUser.token: getRandStr(20)})
        sqlUser = sqlUserSet.first()
        assert sqlUser
    except:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="user is None"
        )
    return sqlUser


async def changeToken(user: UserAuth):
    """
    改变用户token, 不返回值, user为Pydantic模型对象
    """
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
