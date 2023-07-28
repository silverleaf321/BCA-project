import pandas as pd

path = "Salary_Data_cleaned.csv"
df = pd.read_csv(path)

modes = df.mode().iloc[0]
df.fillna(modes, inplace=True)
df.replace({'phD':'PhD', "Master's Degree":"Master's", "Bachelor's Degree":"Bachelor's"}, inplace=True)

null_counts = df.isnull().sum()
total_null_values = null_counts.sum()
print("Total null values:")
print(total_null_values)
df.to_csv(path)

path2 = "Salary_Data.csv"
df2 = pd.read_csv("Salary_Data.csv")
modes = df.mode().iloc[0]
df2.fillna(modes, inplace=True)
df2.to_csv(path2)