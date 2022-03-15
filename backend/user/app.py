__all__ = [
    'user',
]



# 外部依赖项
from fastapi import FastAPI, Request, Response

# 父文件夹依赖
from settings import FILE_PATH
from _ext.sqlalchemy import *

user = FastAPI()


@user.get("/list_book")
async def getBookList(req: Request, filename: str):
    ## 获取个人书架
    pass
