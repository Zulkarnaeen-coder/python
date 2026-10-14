import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')
df =df.dropna()
print(df.head())
print(df.info())
print(df.describe())

print('Species:', df['species'].unique())
print('Islands:', df['island'].unique())


sns.histplot(data=df, x="body_mass_g", bins=20, color="green")
plt.title("Distribution of Penguin Body Mass")
plt.xlabel("Body Mass (grams)")
plt.ylabel("Count")
plt.show()


# KDE only — one smooth curve per species
sns.kdeplot(data=df, x="body_mass_g", hue="species", fill=True)
plt.title("Distribution of Penguin Body Mass Species (KDE)")
plt.xlabel("body mass  (gram)")
plt.ylabel("Density")
plt.show()
# Histogram + KDE together — bars AND the fitted curve
# sns.histplot(data=df, x="flipper_length_mm", kde=True, color="coral")
# plt.title("Flipper Length — Histogram with KDE Curve")
# plt.xlabel("Flipper Length (mm)")
# plt.ylabel("Count")
# plt.show()


sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.title("Flipper Length vs Body Mass by Species")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (grams)")
plt.show()

crr = df.corr(numeric_only=True)
print(crr)
sns.heatmap(crr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Penguin Dataset")
plt.show()