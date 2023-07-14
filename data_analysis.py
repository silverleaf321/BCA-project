import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "C:/Users/User/Silverleaf/Code'23/BCA-project/Salary_Data.csv"

df = pd.read_csv(path)

# scatterplot
sns.scatterplot(data = df, x = df["Age"], y = df["Salary"])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Salary vs Age Scatterplot")
plt.savefig("../plots/Salary_vs_Age_Scatterplot.png")




