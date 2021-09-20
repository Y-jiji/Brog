from fastapi import FastAPI, Header, UploadFile, File, Request
from typing import Optional

from starlette.responses import Response

from auth.public import login_required
from file.utils import writeFile
import asyncio

file = FastAPI()


@file.post("/upload")
@login_required
async def upload(req: Request, file: Optional[UploadFile] = File(None)):
    if file:
        content = await file.read()
        asyncio.create_task(writeFile(file.filename, content))
    else:
        return 0
    return 1