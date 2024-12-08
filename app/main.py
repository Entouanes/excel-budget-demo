from typing import Union

from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend origin
    allow_methods=["POST"],  # Allow POST requests
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
def read_root():
    return {"status": "up"}


@app.post("/summarize/")
def update_item(file: UploadFile = File(...), text: str = Form(None)):
    return {"summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."}
