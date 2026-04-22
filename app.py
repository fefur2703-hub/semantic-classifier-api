from fastapi import FastAPI
from pydantic import BaseModel
import sys

sys.path.append("./source")
from sca_utils import TextClassifier

app = FastAPI()

classifier = TextClassifier(
    model_multiclass_path="./models/model_02_E.h5",
    encoder_multiclass_path="./models/encoder_oneHot_E.pickle",
    model_regression_path="./models/model_01_D2.h5"
)

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(data: TextInput):
    prob_obj, prob_subj = classifier.textClassifier_getSCA_regression(data.text)
    sca_label = classifier.textClassifier_getSCA_multiclass(data.text)

    return {
        "text": data.text,
        "objectivity": float(prob_obj) if prob_obj is not None else None,
        "subjectivity": float(prob_subj) if prob_subj is not None else None,
        "sca_label": sca_label
    }
