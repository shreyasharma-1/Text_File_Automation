"""Use Case: Diabetes Prediction
Perform Exploratory Data Analysis for the Diabetes Dataset.

Dataset: Diabetes.csv
The dataset can be downloaded from https://www.kaggle.com/datasets

Perform the following tasks
1. Load the data in the DataFrame
2. Data Pre-processing
3. Handle the Categorical Data
4. Perform Uni-variate Analysis
5. Perform Bi-variate Analysis"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the Dataset
df = pd.read_csv("Diabetes.csv")

print("=== Dataset Info ===")
print(df.info())
print("\n=== First 5 Rows ===")
print(df.head())

# 2. Data Preprocessing
print("\n=== Missing Values ===")
print(df.isnull().sum())

for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col].fillna(df[col].median(), inplace=True)

df.drop_duplicates(inplace=True)

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype('category')

# 3. Handle Categorical Data
cat_cols = df.select_dtypes(include='category').columns
for col in cat_cols:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())

for col in cat_cols:
    df[col] = df[col].cat.codes

# 4. Univariate Analysis
print("\n=== Univariate Analysis ===")

num_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in num_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True, bins=20, color='skyblue')
    plt.title(f"Distribution of {col}")
    plt.show()

for col in cat_cols:
    plt.figure(figsize=(6,4))
    sns.countplot(x=col, data=df, palette='Set2')
    plt.title(f"Count Plot of {col}")
    plt.show()

# 5. Bi-variate Analysis
print("\n=== Bivariate Analysis ===")

sns.pairplot(df, diag_kind='kde', hue=df.columns[-1])  
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

if 'Outcome' in df.columns:
    for col in num_cols:
        if col != 'Outcome':
            plt.figure(figsize=(6,4))
            sns.boxplot(x='Outcome', y=col, data=df, palette='Set3')
            plt.title(f"{col} vs Outcome")
            plt.show()
