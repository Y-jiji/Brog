from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import CORS_CONFIG

from auth.app import *
from file.app import *


main = FastAPI()

# 挂载子应用
main.mount("/auth", auth, name="auth")
main.mount("/file", file, name='file')

# 挂载中间件
main.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_CONFIG["allow_origins"],
    allow_credentials=CORS_CONFIG["allow_credentials"],
    allow_methods=CORS_CONFIG["allow_methods"],
    allow_headers=CORS_CONFIG["allow_headers"],
)

if __name__ == "__main__":
    # 直接debug运行这个文件, 就会运行自动reload的服务器
    import uvicorn
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor() as executor:
        executor.submit(uvicorn.run, "app:main", reload=True)
