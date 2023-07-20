import pandas as pd

df = pd.read_csv("Salary_Data.csv")

dummies = pd.get_dummies(df["Education Level"])
data_with_dummies = pd.concat([df, dummies], axis = 1)
dummies = pd.get_dummies(df["Gender"])
data_with_dummies = pd.concat([data_with_dummies, dummies], axis = 1)

data_with_dummies.to_csv("Salary_Data_with_dummies.csv", index = False)

df2 = pd.read_csv("Salary_Data_with_dummies.csv")
bools = ["Bachelor", "Master", "High_School", "PhD", "Male", "Female", "Other"]
df[bools] = df[bools].applymap(int)
drop = ["Education Level", "Gender", "Job Title"]
data_with_dummies2 = df2.drop(drop, axis = 1)
data_with_dummies2.to_csv("Salary_Data_with_dummies.csv", index = False)