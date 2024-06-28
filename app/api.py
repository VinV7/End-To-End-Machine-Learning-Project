from flask import Flask, request, jsonify
import joblib
import sys
import os
from dotenv import load_dotenv

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

# Setting up the Flask API
app = Flask(__name__)

# Creating a handler
handler = ModelHandler(preprocessor, rf_classifier)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = handler.predict(data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)