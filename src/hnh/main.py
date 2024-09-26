from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from typing import Union
from transformers import pipeline
from PIL import Image
import numpy as np
import random
import io

app = FastAPI()

html = Jinja2Templates(directory="public")

# load the pytorch version of the model manually
model_name = "julien-c/hotdog-not-hotdog"

@app.get("/hello")
async def root():
    return {"msg": "hello"}

@app.get("/")
async def home(request: Request):
    hotdog = "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQweb_7o7OrtlTP75oX2Q_keaoVYgAhMsYVp1sCafoNEdtSSaHps3n7NtNZwT_ufZGPyH7_9MFcao_r8QWr3Fdz17RitvZXLTU4dNsxr73m6V1scsH3_ZZHRw&usqp=CAE"
    dog = "https://hearingsense.com.au/wp-content/uploads/2022/01/8-Fun-Facts-About-Your-Dog-s-Ears-1024x512.webp"
    image_url = random.choice([hotdog, dog])
    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})

@app.get("/predict")
def hotdog():
    pre = ("Not hot dog", "Hotdog")
    return {"예측 결과는": random.choice(pre)}

@app.post("/Uploadfile/")
async def create_upload_file(file: UploadFile):
    try:
        # read image bytes
        img = await file.read()
        
        model = pipeline("image-classification", model = model_name)

        # 이미지 byte를 PIL 이미지로 변환
        img = Image.open(io.BytesIO(img))

        # perform the prediction
        prediction = model(img)

        # 의존성 모듈 설치해서 오류없이 서버가동

        # if p 값이 배열과 같이 나오면 높은 확률의 값을 추출해서 리턴하기

        return {"filename": file.filename, "예측 결과는..": prediction}

    except Exception as e:
        return {"error": str(e)}
