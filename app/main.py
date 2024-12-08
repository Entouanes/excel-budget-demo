from typing import Union

from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend origin
    allow_methods=["POST"],  # Allow POST requests
    allow_headers=["*"],  # Allow all headers
)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"status": "up"}


@app.put("/summarize/")
def update_item(file: UploadFile = File(...), text: str = Form(None)):
    return {"filename": file.filename, "text": text}
