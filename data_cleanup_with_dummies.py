import pandas as pd

df = pd.read_csv("Salary_Data.csv")

dummies = pd.get_dummies(df["Education Level"])
data_with_dummies = pd.concat([df, dummies], axis = 1)
dummies = pd.get_dummies(df["Gender"])
data_with_dummies = pd.concat([data_with_dummies, dummies], axis = 1)

data_with_dummies.to_csv("Salary_Data_cleaned.csv", index = False)

df2 = pd.read_csv("Salary_Data_cleaned.csv")
bool_cols = ["Bachelor", "Master", "High_School", "PhD", "Male", "Female", "Other"]
df2[bool_cols] = df2[bool_cols].applymap(int)
drop = ["Education Level", "Gender", "Job Title"]
data_with_dummies2 = df2.drop(drop, axis = 1)
data_with_dummies2.to_csv("Salary_Data_cleaned.csv", index = False)

df3 = pd.read_csv("Salary_Data_cleaned.csv")
third = df3.iloc[:, 2]
df3.drop(df3.columns[2], axis = 1, inplace = True)
df3["Salary"] = third
df3.to_csv("Salary_Data_cleaned.csv", index = False)