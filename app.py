from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(data: TextInput):
    
    score = round(random.uniform(0, 1), 2)

    return {
        "text": data.text,
        "subjectivity": score,
        "classification": "alta" if score > 0.6 else "baixa"
    }
