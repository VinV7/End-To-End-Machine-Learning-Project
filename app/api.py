import joblib
from pydantic import BaseModel, Field 
from fastapi import FastAPI, HTTPException
from typing import List
import os
from dotenv import load_dotenv
import sys

# Loading the .env files
load_dotenv()

# Connecting the path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from model_deployment import ModelHandler

# Loading the preprocessor and the model
model_path = os.getenv('MODEL_PATH')
preprocessor_path = os.getenv('PREPROCESSOR_MODEL_PATH')

rf_classifier = joblib.load(model_path)
preprocessor = joblib.load(preprocessor_path)

# Handler
handler = ModelHandler(preprocessor, rf_classifier)

# Fast API Setup
app = FastAPI()

class RequestedItem(BaseModel):
    Age: List[float]
    Number_of_Dependents: List[int] = Field(..., alias="Number of Dependents")
    Zip_Code: List[int] = Field(..., alias="Zip Code")
    Number_of_Referrals: List[int] = Field(..., alias="Number of Referrals")
    Tenure_in_Months: List[int] = Field(..., alias="Tenure in Months")
    Avg_Monthly_Long_Distance_Charges: List[float] = Field(..., alias="Avg Monthly Long Distance Charges")
    Avg_Monthly_GB_Download: List[float] = Field(..., alias="Avg Monthly GB Download")
    Monthly_Charge: List[float] = Field(..., alias="Monthly Charge")
    Total_Charges: List[float] = Field(..., alias="Total Charges")
    Total_Refunds: List[float] = Field(..., alias="Total Refunds")
    Total_Extra_Data_Charges: List[float] = Field(..., alias="Total Extra Data Charges")
    Total_Long_Distance_Charges: List[float] = Field(..., alias="Total Long Distance Charges")
    Total_Revenue: List[float] = Field(..., alias="Total Revenue")
    Satisfaction_Score: List[int] = Field(..., alias="Satisfaction Score")
    Churn_Score: List[int] = Field(..., alias="Churn Score")
    CLTV: List[int]
    Gender: List[str]
    Under_30: List[str] = Field(..., alias="Under 30")
    Senior_Citizen: List[str] = Field(..., alias="Senior Citizen")
    Married: List[str]
    Dependents: List[str]
    City: List[str]
    Phone_Service: List[str] = Field(..., alias="Phone Service")
    Multiple_Lines: List[str] = Field(..., alias="Multiple Lines")
    Internet_Service: List[str] = Field(..., alias="Internet Service")
    Online_Security: List[str] = Field(..., alias="Online Security")
    Online_Backup: List[str] = Field(..., alias="Online Backup")
    Device_Protection_Plan: List[str] = Field(..., alias="Device Protection Plan")
    Premium_Tech_Support: List[str] = Field(..., alias="Premium Tech Support")
    Streaming_TV: List[str] = Field(..., alias="Streaming TV")
    Streaming_Movies: List[str] = Field(..., alias="Streaming Movies")
    Streaming_Music: List[str] = Field(..., alias="Streaming Music")
    Unlimited_Data: List[str] = Field(..., alias="Unlimited Data")
    Contract: List[str]

    class Config:
        populate_by_name = True

@app.post('/predict/')
async def predict(request: List[RequestedItem]):
    try:
        data = [item.dict(by_alias=True, exclude_unset=True, exclude_defaults=True) for item in request]
        print(data)
        data = data[0]
        prediction = handler.predict(data)
        print(prediction)
        return {
            "Prediction": prediction.tolist()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
