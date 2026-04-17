from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI() # 들어오는 경로를 그대로 사용할 경우. Nginx의 리버시 프록시 사용의 경우
# app = FastAPI(root_path="/api") # ALB에서 /api 경로 치환 없이 라우팅한 경우 root_path를 통해 경로 제거.
# Docker 환경에서 안전하게 경로를 찾기 위해 절대 경로를 사용합니다.
base_dir = os.path.dirname(os.path.realpath(__file__))
templates = Jinja2Templates(directory=os.path.join(base_dir, "templates"))

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    welcome_msg = "[두 번째 배포 중입니다] AWS fastAPI에 방문하여 주셔서 감사합니다."
    
    # [핵심 수정] 최신 버전의 FastAPI/Starlette 대응
    # 1. request를 첫 번째 인자(또는 키워드 인자)로 명시합니다.
    # 2. context 딕셔너리를 전달합니다.
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"message": welcome_msg}
    )