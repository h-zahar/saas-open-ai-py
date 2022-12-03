from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.main import generate_snippet

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://tagliner.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello, Hit": "https://api-saas.onrender.com/snippet/?user_input=[your_keyword]"}

@app.get("/snippet")
async def get_generate_snippet(user_input: str):
    content = generate_snippet(user_input)
    if content['status'] == False:
        raise HTTPException(status_code=404, detail=content['msg'])
    return { 'status_code': 200, 'content': content['msg'] }