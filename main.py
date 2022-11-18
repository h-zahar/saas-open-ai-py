from fastapi import FastAPI
from app.main import generate_snippet

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/snippet")
async def get_generate_snippet(user_input: str):
    return generate_snippet(user_input)