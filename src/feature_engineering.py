import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib
from scipy import sparse
import os
from dotenv import load_dotenv

# Loading the .env files
load_dotenv()

# Loading the dataset
clean_path = os.getenv('TELCO_DFCLEAN_PATH')
df = pd.read_csv(clean_path)

# Setting the amount of columns shown
pd.set_option('display.max_columns', None)

# Load the DataFrame
df.head()

# Identifying the Features and saving it to the 'X' Variable 
X = df.drop(columns=['Churn Label'])

# Identifying the Target Value and saving it to the 'y' Variable
y = df['Churn Label']

# Identifying numerical and categorical features
numerical_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns
print(numerical_features)
print(categorical_features)

# Creating the pipelines for the numerical data features
numerical_pipeline = Pipeline(steps=[
    ('scaler', StandardScaler())                 # Standardize features by removing the mean and scaling to unit variance
])

# Creating the pipelines for the categorical data features
categorical_pipeline = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))     # One-hot encode categorical variables
])

# Combining both pipelines into a single ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_pipeline, numerical_features),
        ('cat', categorical_pipeline, categorical_features),
    ]
)

# Fit and transform the features
X_processed = preprocessor.fit_transform(X)

# Turning X_processed (Sparse Matrix) to an Array
X_processed = X_processed.toarray()

# Convert X_processed to DataFrame
X_processed_df = pd.DataFrame(X_processed)

# # Saving the preprocessor 
preprocessor_path = os.getenv('PREPROCESSOR_MODEL_PATH')
joblib.dump(preprocessor, preprocessor_path)

# Save the DataFrame to a CSV file
processed_df = pd.concat([X_processed_df, pd.DataFrame(y, columns=['Churn Label'])], axis=1)
processed_df_path = os.getenv('TELCO_DFPROC_PATH')
processed_df.to_csv(processed_df_path, index=False)

