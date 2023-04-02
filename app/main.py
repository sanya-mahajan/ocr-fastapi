from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
print(BASE_DIR)
templates=Jinja2Templates(directory=BASE_DIR/"templates")
app=FastAPI()

@app.get("/",response_class=HTMLResponse)
def home_view(request: Request):

    return templates.TemplateResponse("home.html",{"request":request,"var":123})  #reqest mandatory and var like string format


@app.post("/")
def home_detail_view():
    return {"message": "Hello World"}