from fastapi import FastAPI
import random as r

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "hello"}

@app.predict("/")
async def predict():
    hotdog = r.randint(1)
    if hotdog == 0:
        return {"It is hotdog"}
    else:
        return {"It is not hotdog"}
