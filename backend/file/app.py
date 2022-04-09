# 全局依赖
import asyncio
from os import close
from sqlite3 import dbapi2
from fastapi import *
from typing import Collection, List, Optional, Dict
import time
from fastapi import Depends

from auth.utils import queryProfile

# 本文件夹依赖
from .utils import *
from file.models import Pdf_File

# 父文件夹依赖
from auth.public import login_required
from _ext.security import getRandStr, secureCtx
from settings import FILE_PATH

#数据库
from file import crud, schemas
from _ext.sqlalchemy import *
from sqlalchemy.orm import Session
from database import *
#数据库初始化，如果没有，则自动创建
Base.metadata.create_all(bind=engine)


from os import path

file = FastAPI()

# pendingDictionary(存储为用户执行的任务的状态(例如上传文件的进度))
penDict: Dict[str, Dict[str, int]] = {}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def getPendingId(userId):
    if userId not in penDict:
        penDict[userId] = {}
    x = getRandStr(5)
    while x in penDict[userId]:
        await asyncio.sleep(1)
    penDict[userId][x] = 0
    return x


@file.post("/upload")
@login_required
async def upload(req: Request, resp: Response, f: Optional[UploadFile] = File(None)):
    if not f:
        return {"status": "failure", "reason": "no file"}

    t = time.time()
    userId = req.cookies["id"]
    taskId = await getPendingId(userId)
    userPenDict = penDict[userId]

    def progPlus(x):
        # 任务进行时调用, 报告任务进度
        userPenDict[taskId] += x

    def popTask():
        # 任务结束时调用, 弹出该任务
        if len(userPenDict) > 1:
            userPenDict.pop(taskId)
        else:
            penDict.pop(userId)

    def insertdb(upF: UploadFile):
        #地址存入数据库
        db = SessionLocal()
        ret = crud.insert_file(db, upF.filename, path.join(FILE_PATH, upF.filename))
        db.close()
    # 提交任务, 返回结果
    asyncio.create_task(
        writeFile(f, progPlus)
    ).add_done_callback(lambda x: popTask())

    print(time.time() - t)
    #存入数据库
    insertdb(f)
    return {"status": "success", "taskId": taskId}


# query upload
@file.websocket("/q/upload")
async def upload(ws: WebSocket):
    userId = ws.query_params["id"]
    token = ws.query_params["token"]
    hashed_token = ws.query_params["hashed_token"]
    if not secureCtx.verify(token, hashed_token):
        return
    await ws.accept()
    while True:
        try:
            taskId = await ws.receive_text()
            allDone = userId not in penDict
            thisDone = allDone or taskId not in penDict[userId]
            progress = penDict[userId][taskId] if not thisDone else -1
            taskState = {
                "taskId": taskId,
                "status": "done" if thisDone else "pending",
                "progress": progress
            }
            await ws.send_json(taskState)
            if allDone:
                await ws.close()
                return
        except WebSocketDisconnect:
            return


@file.websocket("/q-all/upload")
async def upload(ws: WebSocket):
    userId = ws.query_params["id"]
    token = ws.query_params["token"]
    hashed_token = ws.query_params["hashed_token"]
    if not secureCtx.verify(token, hashed_token):
        return
    # 如果用户信息验证没有问题, 可以建立长轮询
    await ws.accept()
    while True:
        # 长轮询, 当用户之前提交的任务全部完成时断开链接
        try:
            await ws.receive_text()
            done = userId not in penDict
            # 用户任务的状态
            taskState = {
                "status": "done" if done else "pending",
                "pendingDict": penDict[userId]
            }
            await ws.send_json(taskState)
            if done:
                await ws.close()
                return
        except WebSocketDisconnect:
            return


@file.get("/wsTestPage/")
async def wsTestPage(req: Request):
    from fastapi.templating import Jinja2Templates
    templates = Jinja2Templates("testPages")
    return templates.TemplateResponse("wsTest.html", context={"request": req, "Chat": "wsTestPage"})




@file.get("/get_file_path")
async def getFilePath(req: Request, bid: str, db: Session = Depends(get_db)):
    obj_tmp = crud.get_file_path(db=db, bid=bid)
    if obj_tmp == False:
        return {'status': 'failure', "message": "读取文件失败"}
    path_tmp = obj_tmp.file_path
    # with open(path_tmp, 'rb') as file:
    #     return {'status':'success', 'content':file.read()}
    return {'status':'success', 'file_obj': path_tmp}


@file.get("/list_book")
async def listUserBook(req: Request):
    try:
        username = queryProfile(req.cookies["token"])
        obj_list = queryBookList(username = username)
        return {'status':'success', 'booklist': obj_list}
    except Exception as e:
        print(e)
        return {'status':'failure', 'msg':"查询失败"}


@file.get("/update_page")
async def updatePersonalPage(req: Request, bid:int, page:int):
    try:
        username = queryProfile(req.cookies["token"])
        updatePage(username=username, bid = bid, page=page)
        return {'status':'success', 'msg':'更新成功'}
    except Exception as e:
        print(e)
        return {'status':'failure', 'msg':"更新失败"}

@file.get("/query_page")
async def queryPersonalPage(req: Request, bid:int):
    try:
        username = queryProfile(req.cookies["token"])
        obj_tmp = queryPage(username=username, bid=bid)
        return {'status':'success', 'page_obj': obj_tmp}
    except Exception as e:
        print(e)
        return {'status':'failure', 'msg':"查询失败"}

@file.get("/test_mongo")
async def testMongo(req: Request):
    try:
        obj = await create_pdf('test', "wwwtest")
        print(obj)
        return {'status':'success'}
    except Exception as e:
        print(e)
        return {'status':'failure', 'msg':"查询失败"}


@file.post("/inverted_index")
async def invertedIndex(req:Request,  bid:int, f: Optional[UploadFile] = File(None)): 
    storagePath = path.join(FILE_PATH, f.filename)
    # print(f.file)
    # file = f.file.encoding
    for line in f.file.readlines():
        line_string = line.decode("gbk")
        line_list = line_string.split()
        if len(line_list) > 1:
            await create_document(line_list[0], line_list[1].split(","), bid)
        else:
            await create_document(line_list[0], [], bid)
        # break
    return {"status":"success"}
    # print(f)
    # byte512 = await f.read(512)
    # while byte512:
    #     with open(storagePath, 'ab') as f:
    #         f.write(byte512)
        
    #     byte512 = await f.read(512)
    # await f.close()
    # with open(storagePath, 'r') as doc:
    #     for line in doc.readlines:
    #         print(line)
    #         break 