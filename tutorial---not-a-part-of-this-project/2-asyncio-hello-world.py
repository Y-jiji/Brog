import asyncio
from random import randint


class AsyncItWrapper:
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


async def mainA(a: str):
    async for x in AsyncItWrapper(range(100)):
        await asyncio.sleep(randint(0, 100) * 1e-5)
        print(f'{a}, {x}')

async def mainS(a: str):
    for x in range(100):
        print(f'{a}, {x}')

asyncio.run(asyncio.wait([mainA("task1"), mainS("task2")]))
