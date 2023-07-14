import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "C:/Users/User/Silverleaf/Code'23/BCA-project/Salary_Data.csv"

df = pd.read_csv(path)

# scatterplot: age vs salary
sns.scatterplot(data = df, x = df["Age"], y = df["Salary"])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Salary vs Age Scatterplot")
plt.savefig("Salary_vs_Age_Scatterplot.png")

plt.figure(figsize=(10, 6))
sns.scatterplot(data = df, x = df["Education Level"], y = df["Salary"])
plt.xlabel("Education Level")
plt.ylabel("Salary")
plt.title("Salary vs Education Level Scatterplot")
plt.savefig("Education_Level_vs_Salary_Scatterplot.png")


