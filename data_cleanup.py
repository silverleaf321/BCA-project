import pandas as pd

path = "Salary_Data_cleaned.csv"
df = pd.read_csv(path)

modes = df.mode().iloc[0]
df.fillna(modes, inplace=True)

null_counts = df.isnull().sum()
total_null_values = null_counts.sum()
print("Total null values:")
print(total_null_values)
df.to_csv(path)