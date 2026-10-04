from pathlib import Path
import json
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
folder = Path(__file__).resolve().parent

model = joblib.load(folder / "best_model.joblib")
features = json.loads((folder / "model_features.json").read_text())


class PredictionRequest(BaseModel):
    records: list[dict]


@app.post("/predict")
def predict(request: PredictionRequest):
    inputs = pd.DataFrame(request.records)[features]
    return {"predictions": model.predict(inputs).tolist()}