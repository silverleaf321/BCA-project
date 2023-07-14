import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "C:/Users/User/Silverleaf/Code'23/BCA-project/Salary_Data.csv"
df = pd.read_csv(path)

sns.set_style("darkgrid")
sns.set_palette("bright")

# scatterplot: age vs salary
sns.scatterplot(data = df, x = df["Age"], y = df["Salary"])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Salary vs Age Scatterplot")
plt.savefig("Salary_vs_Age_Scatterplot.png")

# scatterplot: education level vs salary
plt.figure(figsize=(10, 6))
sns.scatterplot(data = df, x = df["Education Level"], y = df["Salary"])
plt.xlabel("Education Level")
plt.ylabel("Salary")
plt.title("Salary vs Education Level Scatterplot")
plt.savefig("Education_Level_vs_Salary_Scatterplot.png")

# boxplot of salaries
plt.figure(figsize=(10, 6))
sns.boxplot(data = df, x = df["Salary"])
plt.title("Salary Boxplot")
plt.xlabel("Salary")
plt.ylabel("Values")
plt.savefig("Salary_Boxplot.png")
