import data_analysis
import pandas as pd

df = data_analysis.df

for column in df.columns:
    df[column].fillna(df[column].mode().iloc[0], inplace=True)

null_values = df.isnull().sum()
print("Columns with null values:")
print(null_values[null_values > 0])