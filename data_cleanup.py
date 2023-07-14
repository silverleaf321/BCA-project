import pandas as pd

path = "C:/Users/User/Silverleaf/Code'23/BCA-project/Salary_Data.csv"
df = pd.read_csv(path)

# # before
# null_values = df.isnull().sum()
# print("Columns with null values:")
# print(null_values[null_values > 0])
# print("*********************")

for column in df.columns:
    df[column].fillna(df[column].mode().iloc[0], inplace=True)

# after
null_values = df.isnull().sum()
print("Columns with null values:")
print(null_values[null_values > 0])