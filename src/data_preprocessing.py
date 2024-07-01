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
categorical_features = ['Gender', 'Under 30', 'Senior Citizen', 
                        'Dependents', 'Offer', 'Internet Type', 
                        'Contract', 'Churn Label', 'Churn Category',]

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
                      'Monthly Charge', 'Satisfaction Score']

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

# Numerical vs. Numerical
# Tenure in Months vs. Satisfaction Score
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Tenure in Months', y='Satisfaction Score', data=df)
plt.title('Tenure in Months vs. Satisfaction Score')
plt.xlabel('Tenure in Months')
plt.ylabel('Satisfaction Score')
plt.show()

# Monthly Charge vs. Total Charges
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Monthly Charge', y='Total Charges', data=df)
plt.title('Monthly Charge vs. Total Charges')
plt.xlabel('Monthly Charge')
plt.ylabel('Total Charges')
plt.show()

# Categorical vs. Numerical 
# Gender vs. Monthly Charge
plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='Monthly Charge', data=df)
plt.title('Gender vs. Monthly Charge')
plt.xlabel('Gender')
plt.ylabel('Monthly Charge')
plt.show()

# Internet Type vs. Monthly Charge
plt.figure(figsize=(10, 6))
sns.boxplot(x='Internet Type', y='Monthly Charge', data=df)
plt.title('Internet Type vs Monthly Charge')
plt.xlabel('Internet Type')
plt.ylabel('Monthly Charge')
plt.show()

# Categorical vs. Categorical
# Contract vs. Churn Label
plt.figure(figsize=(10, 6))
sns.countplot(x='Contract', hue='Churn Label', data=df)
plt.title('Contract vs. Churn Label')
plt.xlabel('Contract')
plt.ylabel('Count')
plt.show()

# Offer vs. Churn Label
plt.figure(figsize=(10, 6))
sns.countplot(x='Offer', hue='Churn Label', data=df)
plt.title('Offers vs. Churn Label')
plt.xlabel('Offers')
plt.ylabel('Count')
plt.show()

# Dependents vs Churn Label
plt.figure(figsize=(10, 6))
sns.countplot(x='Dependents', hue='Churn Label', data=df)
plt.title('Dependent vs. Churn Label')
plt.xlabel('Dependent')
plt.ylabel('Count')
plt.show()


# End of Analyses

# -. The raw TelCo Dataset CSV contains 7043 rows and 50 columns 
# -. There are missing values in the 'Offer', 'Internet Type', 'Churn Category' and 'Churn Reason' Columns
# -. The reason of the missing values inside the 'Churn Category' and 'Churn Reason' feature is due to values inside of the Churn Label feature
# -. Most users are male although it's only a slight difference to the Female
# -. Most users stayed and did not churn 
# -. There is a linear correlation between Total Charge and Monthly Charge 
# -. Majority of the services offered are accepted
# -. Most users churned due to the offers offered by competitor are better
# -. There's a correlation between the Contract and the likely hood of the customer churning. Customers are more prone to churning when they are in a Month-to-Month contract with the TelCo Provider
# -. There's a correlation between the offers and the likelyhood of the customer churning. Customers that picked the TelCo Company's Offer E is more likely to churn. Customers that picked Offer A or B are most satisfied making it less likely for them to churn
# -. There's a correlation between the Monthly Charge and the Internet Type used by the customers. The correlation shows that customers who use Fiber Optic get charged more rather than Customers who use DSL and Cable
# -. There is no correlation between Tenure in Month and Satisfaction Score, it's equal. Customers who is in their 70 Tenure Months can have both the satisfactory score of 1 and 5.
# -. Whether the customer has people dependent on them, it doesn't affect whether the customer will churn or not.

# Data Cleaning
# Missing Numerical Values on Numerical Features are not found (Skipped)

# Dropping the columns based on the missing values or usefulness
useless_features = ['Customer ID', 'Country', 'State', 'Offer', 'Quarter','Internet Type','Paperless Billing', 'Payment Method', 'Customer Status', 'Churn Category', 'Churn Reason', 'Latitude', 'Longitude', 'Population', 'Referred a Friend']
df = df.drop(useless_features, axis=1)

# Saving the cleaned DataFrame
clean_save_path = os.getenv('TELCO_DFCLEAN_PATH')
df.to_csv(clean_save_path, index=False)