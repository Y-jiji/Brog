# 全局依赖
import asyncio
from os import close
from fastapi import *
from typing import List, Optional, Dict
import time

# 本文件夹依赖
from .utils import writeFile

# 父文件夹依赖
from auth.public import login_required
from _ext.security import getRandStr, secureCtx

file = FastAPI()

# pendingDictionary(存储为用户执行的任务的状态(例如上传文件的进度))
penDict: Dict[str, Dict[str, int]] = {}


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

    # 提交任务, 返回结果
    asyncio.create_task(
        writeFile(f, progPlus)
    ).add_done_callback(lambda x: popTask())

    print(time.time() - t)

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
