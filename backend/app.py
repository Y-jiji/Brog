# 引入本文件依赖, 注意程序入口不能使用'.'记号作为开头的import, 因为程序入口不能判定它所处的文件夹
from auth.app import *
from file.app import *
from settings import CORS_CONFIG, STATIC_PATH


# 引入全局依赖
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


# 实例化ASGI对象
main = FastAPI()  # 主应用
static = StaticFiles(directory=STATIC_PATH)  # 静态文件加载器


# 挂载子应用
main.mount("/auth", auth, name="auth")
main.mount("/file", file, name='file')
main.mount("/static", static, name="static")


# 挂载中间件
main.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_CONFIG["allow_origins"],
    allow_credentials=CORS_CONFIG["allow_credentials"],
    allow_methods=CORS_CONFIG["allow_methods"],
    allow_headers=CORS_CONFIG["allow_headers"],
)


if __name__ == "__main__":
    # 直接debug运行这个文件, 就会运行带有自动reload的服务器
    import uvicorn as uv
    color = 33
    print(f'\033[{color}mapp located in folder:\n------{__file__}')
    uv.run(app='app:main',
           reload=True,
           host='127.0.0.1',
           port=8081)
