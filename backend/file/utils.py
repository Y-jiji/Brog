# 基于全局的依赖
from os import path
from typing import Callable
from fastapi import UploadFile, WebSocket

# 基于本文件夹的依赖项
from file.models import Pdf_File, Personal_File

# 父文件夹依赖
from settings import FILE_PATH
from _ext.sqlalchemy import *

# 外部依赖项
from sqlalchemy.orm import Session

class AsyncIt:
    def __init__(self, obj):
        self._it = iter(obj)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value

async def writeFile(upF: UploadFile, progressPlus: Callable):
    storagePath = path.join(FILE_PATH, upF.filename)
    byte512 = await upF.read(512)
    while byte512:
        with open(storagePath, 'ab') as f:
            f.write(byte512)
        progressPlus(len(byte512))
        byte512 = await upF.read(512)
    await upF.close()


def get_file_path(db: Session, filename: str):
    try:
        return db.query(Pdf_File).filter(Pdf_File.filename == filename, Pdf_File.is_delete == False ).first()
    except:
        return False

def insert_file(db: Session, filename: str, file_path: str):
    db_tmp_file_obj = Pdf_File(filename = filename, file_path = file_path)
    db.add(db_tmp_file_obj)
    db.commit()
    db.refresh(db_tmp_file_obj)
    return db_tmp_file_obj

def delete_file(db: Session, filename: str):
    try:
        db_tmp_file_obj = db.query(Pdf_File).filter(Pdf_File.filename == filename).first()
        db_tmp_file_obj.is_delete = True
        db.commit()
        return True
    except:
        return False



def queryBookList(username: str):
    obj_list = db.query(Personal_File.bid,Personal_File.page, Personal_File.username ,Pdf_File.file_path,Pdf_File.filename,Pdf_File.cover_path).join(Pdf_File,Pdf_File.id == Personal_File.bid).filter(Personal_File.username == username).all()
    return obj_list


def updatePage(username:str, bid:int, page:int):
    obj_tmp = db.query(Personal_File).filter(Personal_File.username == username, Personal_File.bid == bid).first()
    if (obj_tmp):
        obj_tmp.page = page
    else:
        obj_tmp = Personal_File(bid=bid,page=page,username=username)
        db.add(obj_tmp)
    db.commit()
    db.refresh(obj_tmp)

def queryPage(username:str, bid:int):
    obj_tmp = db.query(Personal_File).filter(Personal_File.username == username, Personal_File.bid == bid).first()
    return obj_tmp