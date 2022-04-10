__all__ = [
    'user',
]

# 外部依赖项
from fastapi import FastAPI, Request, Response
import asyncio

# 父文件夹依赖
from settings import FILE_PATH
from _ext.sqlalchemy import *
from database import *

from .schemas import *
from .utils import getAvaliableFields, addAvailableField

user = FastAPI()
Base.metadata.create_all(bind=engine)


@user.get("/list_book")
async def getBookList(req: Request, filename: str):
    ## 获取个人书架
    pass


@user.get("/list_field")
async def listField(req: Request):
    field_list = getAvaliableFields()
    return {'status': 'success', 'fields': field_list}


@user.get("/add_field")
async def addField(req: Request, name: str):
    await addAvailableField(name=name)
    return {'status': 'success'}


@user.post("/init_profile")
async def initProfile(profile: UserProfile, req: Request):
    try:
        if "token" in req.cookies and "id" in req.cookies:
            user_id = req.cookies["id"]
            fields = profile.fields_my
            await create_profile(uid=user_id, field_list=fields)
            return {'status': 'success'}
        else:
            return {'status': 'failure', 'msg': '未登陆'}
    except Exception as e:
        print(e)
        return {'status': 'failure', 'msg': '初始化个人画像失败'}
