from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request

app = FastAPI()

# 정적 파일 경로 설정: static 폴더를 /static 경로로 서빙
app.mount("/static", StaticFiles(directory="static"), name="static")

# 템플릿 디렉터리 설정
templates = Jinja2Templates(directory="templates")

# 루트 경로
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 서비스 워커 서빙
@app.get("/service-worker.js")
async def service_worker():
    return StaticFiles(directory="static").__call__(scope=None, receive=None, send=None)

# 매니페스트 서빙
@app.get("/manifest.json")
async def manifest():
    return StaticFiles(directory="static").__call__(scope=None, receive=None, send=None)
