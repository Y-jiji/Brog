async def funcApp(scope, receive, send):
    assert scope['type'] == 'http'
    await send({'type': 'http.response.start', 'status': 200, 'headers': [[b'content-type', b'text/plain'], ]})
    await send({'type': 'http.response.body', 'body': b'Hello, world!', })

if __name__ == "__main__":
    # 直接debug运行这个文件, 就会运行自动reload的服务器
    import uvicorn as uv
    uv.run(app='%s:funcApp' % __file__.split("/")
           [-1].split("\\")[-1].split(".")[0],
           reload=True,
           host='127.0.0.1',
           port=8081)
