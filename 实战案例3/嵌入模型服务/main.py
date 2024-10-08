from fastapi import FastAPI, Request
import uvicorn
from 向量编码器 import 向量编码器

app = FastAPI()

@app.get("/")
async def read_root():
    return {"hello word":"这里是向量编码服务"}

app.向量编码器instance = None

@app.on_event('startup')
def init_data():
    app.向量编码器instance = 向量编码器()

@app.post("/api/embedding/encode")
async def 向量编码(request: Request):
    data = await request.json()
    print(data)
    input_str= data["input"]
    return_result = app.向量编码器instance.向量编码(input_str)
    return return_result
    # return data

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8902)