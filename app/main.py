from typing import Union

from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from utils.get_summary import get_summary


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Frontend origin
    allow_methods=["POST"],  # Allow POST requests
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
async def read_root():
    return {"status": "up"}


@app.post("/summarize/")
async def update_item(file: UploadFile = File(...), text: str = Form(None)):
    try:
        title, summary = await get_summary(file.file, text)
        return {"summary": summary, "title": title}
    except Exception as e:
        return {"summary": str(e)}
    
