import uvicorn                          # uvicorn이라는 모듈을 가져옴
from fastapi import FastAPI             # fastapi에서 FastAPI 모듈을 가져옴
from users import router as u_router    # users에서 router 모듈을 가져오고 이를 u_router라고 부르기로 정의

app = FastAPI()

app.include_router(u_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host = "0.0.0.0",
        port = 8000,
        reload = True
    )