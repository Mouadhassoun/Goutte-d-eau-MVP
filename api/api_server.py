import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = FastAPI(title="API Goutte d’eau")

class MeteoInput(BaseModel):
    temperature: float
    humidite: float
    pression: float
    vent: float


@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API Goutte d'eau — utilisez /docs pour tester les prédictions."}

@app.post("/predict")
def predict_rain(data: MeteoInput):
    model = joblib.load(os.path.join(BASE_DIR, "models", "voting_model.pkl"))
    scaler = joblib.load(os.path.join(BASE_DIR, "models", "scaler.pkl"))
    X = np.array([[data.temperature, data.humidite, data.pression, data.vent]])
    X_scaled = scaler.transform(X)
    proba = model.predict_proba(X_scaled)[0][1]
    return {"probabilite_pluie": round(float(proba), 3)}

