from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model.joblib"

model = joblib.load(MODEL_PATH)

app = FastAPI(title="Titanic Survival Prediction API")


class Passenger(BaseModel):
    Pclass: int = Field(ge=1, le=3)
    Sex: int = Field(ge=0, le=1)
    Age: float = Field(ge=0, le=100)
    SibSp: int = Field(ge=0, le=20)
    Parch: int = Field(ge=0, le=20)
    Fare: float = Field(ge=0)
    Embarked: int = Field(ge=0, le=2)


@app.get("/")
def home():
    return {"message": "Titanic Survival Prediction API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(passenger: Passenger):
    data = pd.DataFrame([passenger.model_dump()])
    data = data[
        ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
    ]

    prediction = int(model.predict(data)[0])

    return {
        "survived": prediction,
        "prediction": "Survived" if prediction == 1 else "Did not survive",
    }
