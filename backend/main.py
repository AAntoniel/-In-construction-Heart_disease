from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel
import pandas as pd

with open("backend/model_heart_dis.pkl", "rb") as f:
    model = pd.read_pickle("backend/model_heart_dis.pkl")

app = FastAPI(title="Heart Disease Risk Assessment API")

class HeartDisease(BaseModel):
    age: int
    sex: int
    chest_pain: int
    restbps: int
    chol: int
    max_heart_rate: int
    exc_angina: int

    def features(self):
        user_input_dict = {
            "age": self.age,
            "sex": self.sex,
            "chest_pain": self.chest_pain,
            "restbps": self.restbps,
            "chol": self.chol,
            "max_heart_rate": self.max_heart_rate,
            "exc_angina": self.exc_angina,
        }

        df_features = pd.DataFrame([user_input_dict])

        return df_features

@app.get("/")
def home():
    return {"message": "Welcome to the heart disease assessment API"}

@app.post("/predict")
def predict_disease(data: HeartDisease):
    features = data.features()

    proba = model["model"].predict_proba(features[model["features"]])[:, 1][0]

    return {
            "input": data.dict(),
            "Prediction": float(proba),
            "Classification": "High Risk" if proba > 0.5 else "Low Risk"
           }
