from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(data: TextInput):
    return {
        "text": data.text,
        "message": "API funcionando"
    }
