from fastapi import FastAPI, HTTPException
from app.main import generate_snippet

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/snippet")
async def get_generate_snippet(user_input: str):
    content: dict['status': True | False, 'msg': str] = generate_snippet(user_input)
    if content['status'] == False:
        raise HTTPException(status_code=404, detail=content['msg'])
    return { 'status_code': 200, 'content': content['msg'] }