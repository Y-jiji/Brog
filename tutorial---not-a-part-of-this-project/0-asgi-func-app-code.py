import uvicorn as uv


async def funcApp(scope, receive, send):
    assert scope['type'] == 'http'
    await send({'type': 'http.response.start', 'status': 200, 'headers': [[b'content-type', b'text/plain'], ]})
    await send({'type': 'http.response.body', 'body': b'Hello, world!', })


uv.run(funcApp, reload=True, host='127.0.0.1', port=8081)