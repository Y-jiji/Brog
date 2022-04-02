# 基于全局的依赖
from os import path
from typing import Callable
from fastapi import UploadFile, WebSocket

# 基于本文件夹的依赖项
from file.models import Pdf_File

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

