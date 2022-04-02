# 基于本文件夹的依赖项
from grpc import Status
from note.models import Note



# 基于父文件夹的依赖项
from _ext.sqlalchemy import *


async def insertNote(email: str , note_name: str, content: str, status: bool):
    db_tmp_note_obj = Note(email=email, note_name=note_name, content=content, status=status)
    print(db_tmp_note_obj)
    db.add(db_tmp_note_obj)
    db.commit()
    db.refresh(db_tmp_note_obj)
    return db_tmp_note_obj

async def queryNote(email: str):
    # tmp_list = [1,2]
    tmp_list = db.query(Note).filter(Note.email == email).all()
    print(tmp_list)
    return tmp_list

async def updateNoteStatus(nid: int):
    db_tmp_note_obj = db.query(Note).filter(Note.id == nid).first()
    db_tmp_note_obj.status = 1
    db.commit()
    db.refresh(db_tmp_note_obj)