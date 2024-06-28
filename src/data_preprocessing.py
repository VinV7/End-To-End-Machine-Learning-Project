import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import os
from dotenv import load_dotenv 

# Set plotting style
sns.set(style="whitegrid")

# Loading the .env files
load_dotenv()

# Loading the dataset 
dataset_path = os.getenv("RAW_TELCO_DATASET_PATH")
df = pd.read_csv(dataset_path)

# Setting the amount of columns shown
pd.set_option('display.max_columns', None)

# Display the first few rows 
df.head()

# Dataset Info
df.info()

# Basic Stats
df.describe()

# Check for missing values
df.isnull().sum()

# Univariate Analysis
# Categorical Features
categorical_features = ['Gender', 'Under 30', 'Senior Citizen', 'Married', 
                        'Dependents', 'Offer',
                        'Phone Service', 'Internet Service', 'Internet Type', 
                        'Contract', 'Paperless Billing', 'Payment Method', 
                        'Customer Status', 'Churn Label', 'Churn Category', 'Churn Reason']

# Plotting bar plots for categorical features
for feature in categorical_features:
    plt.figure(figsize=(8, 5))
    if df[feature].nunique() <= 10:
        sns.countplot(x=feature, data=df)
    else:
        # For features with more than 10 unique values, display value counts
        value_counts = df[feature].value_counts()
        plt.bar(value_counts.index, value_counts.values)
        plt.xticks(rotation=45)
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.title(f'{feature} Distribution')
    plt.tight_layout()
    plt.show()

# Numerical Features
numerical_features = ['Age', 'Number of Dependents', 'Tenure in Months', 
                      'Avg Monthly Long Distance Charges', 'Monthly Charge']

# Plotting histograms for numerical features
for feature in numerical_features:
    plt.figure(figsize=(8, 5))
    plt.hist(df[feature], bins=20, edgecolor='black')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {feature}')
    plt.grid(True)
    plt.show()

# Bivariate Analysis
# Tenure in Months vs. Monthly Charge
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Tenure in Months', y='Monthly Charge', data=df)
plt.title('Tenure in Months vs. Monthly Charge')
plt.xlabel('Tenure in Months')
plt.ylabel('Monthly Charge')
plt.show()

# Monthly Charge vs. Total Charges
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Monthly Charge', y='Total Charges', data=df)
plt.title('Monthly Charge vs. Total Charges')
plt.xlabel('Monthly Charge')
plt.ylabel('Total Charges')
plt.show()


# End of Analyses

# -. The raw TelCo Dataset CSV contains 7043 rows and 50 columns 
# -. There are missing values in the 'Offer', 'Internet Type', 'Churn Category' and 'Churn Reason'
# -. The reason of the missing values inside the 'Churn Category' and 'Churn Reason' feature is due to values inside of the Churn Label feature
# -. Most users are male although it's only a slight difference to the Female
# -. Most users stayed and did not churn 
# -. There slight difference in the monthly charge between Female and Male users benefitting Female Users slightly
# -. There is a linear correlation between Total Charge and Monthly Charge 
# -. Majority of the services offered are accepted
# -. Most users churned due to the offers offered by competitor are better

# Data Cleaning
# Missing Numerical Values on Numerical Features are not found (Skipped)

# Dropping the columns based on the missing values or usefulness
useless_features = ['Customer ID', 'Country', 'State', 'Offer', 'Quarter','Internet Type','Paperless Billing', 'Payment Method', 'Customer Status', 'Churn Category', 'Churn Reason', 'Latitude', 'Longitude', 'Population', 'Referred a Friend']
df = df.drop(useless_features, axis=1)

# Saving the cleaned DataFrame
clean_save_path = os.getenv('TELCO_DFCLEAN_PATH')
df.to_csv(clean_save_path, index=False)