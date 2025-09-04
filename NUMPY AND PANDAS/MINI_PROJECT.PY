"""Use Case: Perform the Outlier detection for the given dataset ie.datasetExample
Dataset: datasetExample.csv

Perform the following task
1.Load the data in the DataFrame.
2.Detection of Outliers"""

import pandas as pd
import numpy as np

df = pd.read_csv("datasetExample.csv")
print("First 5 rows of the dataset:")
print(df.head())

numeric_df = df.select_dtypes(include=np.number)
print("\nNumeric columns considered for outlier detection:")
print(numeric_df.columns.tolist())

def detect_outliers_iqr(data):
    outlier_indices = []
    for col in data.columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)
        outlier_list = data[(data[col] < lower_bound) | (data[col] > upper_bound)].index
        outlier_indices.extend(outlier_list)
    return list(set(outlier_indices))

outlier_rows_iqr = detect_outliers_iqr(numeric_df)

print("\n[IQR Method] Outlier Rows:")
print(df.loc[outlier_rows_iqr])
