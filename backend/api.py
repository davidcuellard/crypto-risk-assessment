from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# Load the trained model
model = joblib.load('risk_assessment_model.pkl')

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the input data model
class RiskAssessmentInput(BaseModel):
    volatility: float
    liquidity: float
    momentum: float
    avg_sentiment: float

# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Cryptocurrency Risk Assessment API"}

# Define the prediction endpoint
@app.post("/predict")
def predict_risk(input_data: RiskAssessmentInput):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data.dict()])

    # Make prediction
    prediction = model.predict(input_df)

    # Map prediction to risk level
    risk_level = 'High Risk' if prediction[0] == 1 else 'Low Risk'

    return {
        "risk_level": risk_level,
        "prediction": int(prediction[0])
    }

# Load historical data
historical_data = pd.read_csv('../data/processed/final_dataset.csv')

# Define endpoint for historical data
@app.get("/historical-data")
def get_historical_data():
    # Select relevant columns and convert to records
    data = historical_data[['date', 'price', 'risk_label']].copy()
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')  # Format date for consistency
    data.rename(columns={'risk_label': 'risk_score'}, inplace=True)
    return data.to_dict(orient='records')
