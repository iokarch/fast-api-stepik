from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("index.html")

@app.post("/calculate")
async def root(num1: int, num2:int):
    return {'result': num1+num2}