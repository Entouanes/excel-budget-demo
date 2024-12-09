from typing import Union

from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from utils.summary_generator import generate_summary
from utils.report import Report


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
async def update_item(file: UploadFile = File(...), constraints: str = Form(None)):
    try:
        # Extract data from the report as a string
        report = Report(file.file)
        report_str = report.get_report()

        try:
            title, summary = await generate_summary(report_str, constraints)
            return {"summary": summary, "title": title}
        
        except Exception as e:
            return {"summary": str(e)}
        
    except Exception as e:
        return {"summary": str(e)}