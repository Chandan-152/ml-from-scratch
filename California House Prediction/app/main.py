import pandas as pd
from fastapi import FastAPI
from app.model import model
from app.schema import PredictionRequest, PredictionResponse

app = FastAPI()

columns = [
    'longitude', 'latitude', 'housing_median_age', 'total_rooms',
    'total_bedrooms', 'population', 'households', 'median_income',
    'ocean_proximity'
]

@app.post("/predict", response_model=PredictionResponse)
def predict(data: PredictionRequest):
    # Convert named fields to dict and then DataFrame
    df = pd.DataFrame([data.dict()])  # key names = column names
    prediction = model.predict(df)
    return {"prediction": float(prediction[0])}
