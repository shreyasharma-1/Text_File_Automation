"""Q1)Perform Exploratory Data Analysis for the dataset Mall Customers. The dataset
 can be downloaded from https://www.kaggle.com/datasets"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Dataset
df = pd.read_csv("Mall_customers.csv")

print("=== Dataset Overview ===")
print(df.info())
print(df.head())

# 2. Data Preprocessing
print("\n=== Missing Values ===")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype('category')

# 3. Handle Categorical Data
cat_cols = df.select_dtypes(include='category').columns
print("\n=== Categorical Column Value Counts ===")
for col in cat_cols:
    print(f"\n{col}:")
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

plt.figure(figsize=(6,4))
sns.countplot(x='Gender', data=pd.read_csv("Mall_Customers.csv"), palette='Set2')
plt.title("Count of Customers by Gender")
plt.show()

# 5. Bivariate Analysis
print("\n=== Bivariate Analysis ===")

sns.pairplot(df)
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='Age', y='Spending Score (1-100)', data=pd.read_csv("Mall_Customers.csv"), hue='Gender')
plt.title("Age vs Spending Score")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', data=pd.read_csv("Mall_Customers.csv"), hue='Gender')
plt.title("Income vs Spending Score")
plt.show()

# 6. Boxplots for Distribution by Gender
plt.figure(figsize=(6,4))
sns.boxplot(x='Gender', y='Annual Income (k$)', data=pd.read_csv("Mall_Customers.csv"), palette='Set3')
plt.title("Annual Income by Gender")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x='Gender', y='Spending Score (1-100)', data=pd.read_csv("Mall_Customers.csv"), palette='Set3')
plt.title("Spending Score by Gender")
plt.show()

"""Q2)Perform Exploratory Data Analysis for the dataset salary_data. The dataset can
be downloaded from https://www.kaggle.com/datasets"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Dataset
df = pd.read_csv("salary_Data.csv")

print("=== Dataset Overview ===")
print(df.info())
print(df.head())

# 2. Data Preprocessing
print("\n=== Missing Values ===")
print(df.isnull().sum())

for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col].fillna(df[col].median(), inplace=True)

df.drop_duplicates(inplace=True)

# 3. Statistical Summary
print("\n=== Statistical Summary ===")
print(df.describe().T)

# 4. Univariate Analysis
print("\n=== Univariate Analysis ===")

for col in df.select_dtypes(include=['int64', 'float64']).columns:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True, bins=15, color='skyblue')
    plt.title(f"Distribution of {col}")
    plt.show()

# 5. Bivariate Analysis
print("\n=== Bivariate Analysis ===")

if 'YearsExperience' in df.columns and 'Salary' in df.columns:
    plt.figure(figsize=(6,4))
    sns.scatterplot(x='YearsExperience', y='Salary', data=df, color='blue')
    plt.title("Years of Experience vs Salary")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.show()

    plt.figure(figsize=(6,4))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

# 6. Pairplot (if multiple columns)
if df.shape[1] > 2:
    sns.pairplot(df)
    plt.show()

"""Q3)Perform Exploratory Data Analysis for the dataset Social Network Ads. The dataset
can be downloaded from https://www.kaggle.com/datasets"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Dataset
df = pd.read_csv("Social_Network_Ads.csv")

print("=== Dataset Overview ===")
print(df.info())
print(df.head())

# 2. Data Preprocessing
if 'User ID' in df.columns:
    df.drop(columns=['User ID'], inplace=True)

print("\n=== Missing Values ===")
print(df.isnull().sum())

for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col].fillna(df[col].median(), inplace=True)

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype('category')

for col in df.select_dtypes(include='category').columns:
    df[col] = df[col].cat.codes

# 3. Statistical Summary
print("\n=== Statistical Summary ===")
print(df.describe().T)

# 4. Univariate Analysis
print("\n=== Univariate Analysis ===")

for col in df.select_dtypes(include=['int64', 'float64']).columns:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True, bins=15, color='skyblue')
    plt.title(f"Distribution of {col}")
    plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='Purchased', data=df, palette='Set2')
plt.title("Purchase Distribution")
plt.show()

# 5. Bivariate Analysis
print("\n=== Bivariate Analysis ===")

plt.figure(figsize=(6,4))
sns.scatterplot(x='Age', y='EstimatedSalary', hue='Purchased', data=df, palette='Set1')
plt.title("Age vs Estimated Salary (by Purchase)")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x='Purchased', y='Age', data=df, palette='Set3')
plt.title("Age by Purchase")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x='Purchased', y='EstimatedSalary', data=df, palette='Set3')
plt.title("Estimated Salary by Purchase")
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# 6. Pairplot for Relationships
sns.pairplot(df, hue='Purchased', palette='husl')
plt.show()
