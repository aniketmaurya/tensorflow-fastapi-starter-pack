import os

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

CWD = os.getcwd()
app = FastAPI()

app.mount("/static", StaticFiles(directory=f'{CWD}/app/static'), name='static')

templates = Jinja2Templates(directory=f'{CWD}/app/templates')


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "id": id
    })


@app.get('/predict')
def predict():
    # do something
    return 'predictions'


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
