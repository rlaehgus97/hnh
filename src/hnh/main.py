from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    print({"msg": "hello"})
