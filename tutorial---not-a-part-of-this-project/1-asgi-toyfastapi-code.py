from typing import *


class ToyFastApi:
    def __init__(self, name) -> None:
        self.router = {}
        self.name = name

    def route(self, path: str, method: str):
        def decorator(func: Callable):
            self.router[(path.removesuffix('/') + "/", method.lower())] = func
            return func
        return decorator

    async def __call__(self, scope, receive, send):
        scope["app"] = self.name
        func = self.router[
            scope['path'].removesuffix('/') + "/",
            scope['method'].lower()
        ]

        async def make_response():
            body, content_type = await func(await receive(), scope)
            await send({'type': 'http.response.start', 'status': 200, 'headers': [[b'content-type', str(content_type).encode('GBK')], ]})
            await send({'type': 'http.response.body', 'body': body, })

        await make_response()


app = ToyFastApi("app")


@app.route("/apple/good", "GET")
async def indexPage(received, scope):
    return """
<div style='margin: 0 auto; text-align:center'>
<h1 style='margin: 0 auto; text-align:center'> Apple </h1>
<h2 style='margin: 0 auto; text-align:center'> This is an apple. I like apples. Apples are good for ourselves. </h2>
<img style='margin: 0 auto; text-align:center' src="http://localhost:8000/img?id=goodapple.jpg">
<h2 style='margin: 0 auto; text-align:center'><a href="/apple/bad/">Bad Apple-></a></h2>
</div>
""".encode('GBK'), 'text/html'


@app.route("/apple/bad", "GET")
async def anotherPage(received, scope):
    return """
<div style='margin: 0 auto; text-align:center'>
<h1 style='margin: 0 auto; text-align:center'> Bad Apple </h1>
<h2 style='margin: 0 auto; text-align:center'>This is an bad apple. Residents in 東方幻想郷 like bad apples. But bad apples are bad for their health.<h2>
<img style='margin: 0 auto; text-align:center' src="http://localhost:8000/img?id=badapple.png">
<h2 style='margin: 0 auto; text-align:center'><a href="/apple/good/">Good Apple-></a></h2>
</div>
""".encode('GBK'), 'text/html'


@app.route("/img", "GET")
async def giveImg(received, scope):
    query = scope["query_string"].decode('GBK').split("&")
    queryDict = {}
    for x in query:
        y = x.split("=")
        queryDict[y[0]] = y[1]
    import os.path as path
    with open(path.join(path.dirname(__file__), "img", queryDict["id"]), 'rb') as f:
        return f.read(), 'img/%s' % queryDict["id"].split(".")[-1]


@app.route("/", "GET")
async def index(recieved, scope):
    return """
<h1 style='margin: 0 auto; text-align:center'>There are two apples</h1>
<h2 style='margin: 0 auto; text-align:center'><a href="/apple/good/">Good Apple-></a></h2>
<h2 style='margin: 0 auto; text-align:center'><a href="/apple/bad/">Bad Apple-></a></h2>
""".encode('GBK'), 'text/html'


if __name__ == "__main__":
    # 直接debug运行这个文件, 就会运行自动reload的服务器
    import uvicorn as uv
    uv.run(app='%s:app' % __file__.split("/")
           [-1].split("\\")[-1].split(".")[0],
           reload=True,
           host='127.0.0.1',
           port=8081)
