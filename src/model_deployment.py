import joblib
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

# Creating a class for Data Preprocessing and Model Prediction
class ModelHandler:
    def __init__(self, preprocessor, model):
        self.preprocessor = preprocessor
        self.model = model
    
    def preprocess_data(self, new_data):
        df = pd.DataFrame(new_data)
        processed_data = self.preprocessor.transform(df)
        return processed_data
    
    def predict(self, new_data):
        processed_data = self.preprocess_data(new_data)
        predictions = self.model.predict(processed_data)
        return predictions
