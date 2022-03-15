__all__ = [
    'note',
]
# 父文件夹依赖
from _ext.security import *

# 基于本文件夹的依赖项
from .utils import *
from .schemas import *  # 前端传输过来的数据类型

# 外部依赖项
from fastapi import FastAPI, Request, Response
Base.metadata.create_all(bind=engine)

note = FastAPI()



@note.get("/list_note")
async def getNoteList(req: Request, email: str):
    ## 获取个人笔记
    try:
        note_list_tmp = await queryNote(email)
        return {'status':'success', 'notes':note_list_tmp}
    except:
        return {'status':'failure', 'msg':'获取个人笔记错误'}

@note.post("/save_note")
async def saveDraft(note: UserNote,req: Request):
    ## 保存草稿
    try:
        note_obj_tmp = await insertNote(email=UserNote.email,
            note_name=UserNote.note_name,
            content=UserNote.content,
            status=False
        )
        return {'status':'success'}
    except:
        return {'status':'failure'}


@note.post("/release_note")
async def releaseNote(nid:int, req:Request):
    try:
        await updateNoteStatus(nid)
        return {'status':'success'}
    except:
        return {'status':'failure'}