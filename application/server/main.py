import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse

from application.components import predict, read_imagefile

app = FastAPI(title='Tensorflow Web app Starter Pack', description='by Aniket Maurya')


@app.get('/')
async def index():
    return RedirectResponse(url='/docs')


@app.post("/api/predict")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)

    return prediction


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
