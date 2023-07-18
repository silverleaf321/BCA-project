import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import data_cleanup

df = data_cleanup.df

sns.set_style("darkgrid")
sns.set_palette("pastel")

# scatterplot: age vs salary
plt.figure(figsize=(10, 6))
scatterplot = sns.scatterplot(data = df, x = df["Age"], y = df["Salary"], c = df["Years of Experience"], cmap = "viridis_r", edgecolors = "black")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary Scatterplot")
# color bar stuff
sm = cm.ScalarMappable(cmap="viridis_r")
sm.set_array(df["Years of Experience"])
cbar = plt.colorbar(sm)
cbar.set_label("Years of Experience")
# plt.savefig("Age_vs_Salary_Scatterplot.png")

# barplot: education level vs salary
plt.figure(figsize=(10, 6))
sns.barplot(data = df, x = df["Education Level"], y = df["Salary"])
plt.xlabel("Education Level")
plt.ylabel("Salary")
plt.title("Education Level vs Salary Barplot")
# plt.savefig("Education_Level_vs_Salary_Barplot.png")

# boxplot: salaries
plt.figure(figsize=(10, 6))
sns.boxplot(data = df, x = df["Salary"]) 
plt.title("Salary Boxplot")
plt.xlabel("Salary")
plt.ylabel("Values")
# plt.savefig("Salary_Boxplot.png")

# barplot: gender vs salary
plt.figure(figsize=(10, 6))
sns.barplot(data = df, x = df["Gender"], y = df["Salary"])
plt.xlabel("Gender")
plt.ylabel("Salary")
plt.title("Gender vs Salary Barplot")
# plt.savefig("Gender_vs_Salary_Barplot.png")  

# sibe by side boxplot: gender vs salary
plt.figure(figsize=(10, 6))
combined_df = [df["Gender"], df["Salary"]]
labels = ["Gender", "Salary"]
df = pd.DataFrame(dict(zip(labels, combined_df)))
sns.boxplot(data = df, y = "Gender", x = "Salary")
# plt.savefig("Gender_vs_Salary_Boxplot.png")

# stacked bar graph: education level vs gender
# weirdest error ever
plt.figure(figsize = (10, 6))
sns.countplot(data = df, x = df["Education Level"], hue = df["Gender"])
plt.xlabel("Education Level")
plt.ylabel("Count")
# plt.savefig("Education_Level_vs_Gender_Countplot.png")