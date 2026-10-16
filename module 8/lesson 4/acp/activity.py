import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("planets")
df = df.dropna()
print(df.head())
print(df.info())
print(df.describe())

print("Method",df["method"].unique())
print("Year",df["year"].unique())

sns.histplot(data = df,x ="orbital_period",bins = 20,color = "red" )
plt.title("Distribution of Orbital Period")
plt.xlabel("Orbital Period (days)")
plt.ylabel("Count")
plt.show()

sns.kdeplot(data = df,x = "orbital_period",hue = "method",fill = True)
plt.title("Distribution of Orbital Period by Method (KDE)")
plt.xlabel("Orbital Period (days)")
plt.ylabel("Density")
plt.show()


sns.scatterplot(data = df,x = "orbital_period",y = "year",hue = "method")
plt.title("Orbital Period vs Year by Method")
plt.xlabel("Orbital Period (days)")
plt.ylabel("Year")
plt.show()


crr = df.corr(numeric_only=True)
print(crr)
sns.heatmap(crr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Planets Dataset")
plt.show()
