import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import joblib
from scipy import sparse
import os
from dotenv import load_dotenv

# Loading the .env files
load_dotenv()

# Loading the dataset
processed_df_path = os.getenv('TELCO_DFPROC_PATH')
df = pd.read_csv(processed_df_path)

# Setting the amount of columns shown
pd.set_option('display.max_columns', None)


# Splitting
X = df.drop(columns=['Churn Label'])
y = df['Churn Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42) # The Machine Learning algorithm used for this project is Random Forest
rf_classifier.fit(X_train, y_train)

# Model Prediction and Evaluation
y_pred = rf_classifier.predict(X_test)
print(classification_report(y_test, y_pred))

# Saving the Model
model_path = os.getenv('MODEL_PATH')
joblib.dump(rf_classifier, model_path)
