import pandas as pd

df = pd.read_csv("Salary_Data.csv")

dummies = pd.get_dummies(df["Education Level"])
data_with_dummies = pd.concat([df, dummies], axis = 1)

data_with_dummies.to_csv("Salary_Data_with_dummies.csv", index = False)