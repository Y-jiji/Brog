# 全局依赖
import asyncio
from fastapi import *
from typing import Optional, Dict

# 本文件夹依赖
from .utils import writeFile
from .description import *

# 父文件夹依赖
from auth.public import login_required
from _ext.security import getRandStr, secureCtx

# 实例化应用对象
file = FastAPI()


penDict: Dict[str, Dict[str, int]] = {}
"""
pendingDictionary(存储为用户执行的任务的状态(例如上传文件的进度))
第一层索引: 用户名; 
    第二层索引: 任务id; 
        值: 代表任务进度的数字
"""


async def getPendingId(userId):
    """
    获取一个新任务的pendingId, 并把它加入penDict
    """
    if userId not in penDict:
        penDict[userId] = {}
    x = getRandStr(5)
    while x in penDict[userId]:
        await asyncio.sleep(1)
    penDict[userId][x] = 0
    return x


@file.post("/upload", description=describe_upload)
@login_required
async def upload(req: Request, resp: Response, f: Optional[UploadFile] = File(None)):
    if not f:
        return {"status": "failure", "reason": "no file"}

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

    return {"status": "success", "taskId": taskId}


# query upload
@file.websocket("/q/upload")
async def queryUpload(ws: WebSocket):
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
async def queryAllUpload(ws: WebSocket):
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


# 下面都是测试时才使用的接口


@file.get("/wsTestPage/")
async def wsTestPage(req: Request):
    from fastapi.templating import Jinja2Templates
    templates = Jinja2Templates("testPages")
    return templates.TemplateResponse("wsTest.html", context={"request": req, "Chat": "wsTestPage"})
