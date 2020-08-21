import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse

from application.components import predict, read_imagefile

app = FastAPI(title='Tensorflow Web app Starter Pack', description='<h2>Try this app by uploading any image with `predict/image`</h2><br>by Aniket Maurya')


@app.get('/', include_in_schema=False)
async def index():
    return RedirectResponse(url='/docs')


@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)

    return prediction


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
