# 基于全局的依赖
from os import path
from typing import Callable
from fastapi import UploadFile, WebSocket


# 父文件夹依赖
from settings import FILE_PATH


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
