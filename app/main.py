from fastapi import FastAPI, Request,Depends,File,UploadFile,HTTPException
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates
import pathlib, uuid
import os,io
from functools import lru_cache
from pydantic import BaseSettings
from PIL import Image

class Settings(BaseSettings):
    debug: bool = False
    echo_on: bool = False

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()


settings=get_settings()
debug=settings.debug
BASE_DIR = pathlib.Path(__file__).parent

UPLOAD_DIR = BASE_DIR / "uploads"

print(BASE_DIR)
templates=Jinja2Templates(directory=BASE_DIR/"templates")
app=FastAPI()

@app.get("/",response_class=HTMLResponse)
def home_view(request: Request, settings: Settings = Depends(get_settings)):
    print(settings.debug)

    return templates.TemplateResponse("home.html",{"request":request,"var":123})  #reqest mandatory and var like string format


@app.post("/echo/",response_class=FileResponse)


async def echo_view(file:UploadFile = File(...), settings: Settings=Depends(get_settings)):
    if not settings.echo_on:
        raise HTTPException(detail="invalid endpoint",status_code=400)

    UPLOAD_DIR.mkdir(exist_ok=True)
    file_byte_str= io.BytesIO(await file.read())
    try:
        img = Image.open(file_byte_str)
    except:
        raise HTTPException(detail="Invalid image", status_code=400)
    fname = pathlib.Path(file.filename)
    fext = fname.suffix # .jpg, .txt

    destination = UPLOAD_DIR / f"{uuid.uuid1()}{fext}"
    img.save(destination)
    return destination