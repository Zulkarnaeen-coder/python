import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

df = df.dropna()
print(df.head())
print(df.info())
print(df.describe())

print("Sex:",df["sex"].unique())
print("class:",df["class"].unique())

sns.barplot(x="survived", y="age", data=df, hue="sex")
plt.title("Average Age of Survivors by Sex")
plt.xlabel("Survived")
plt.ylabel("age")
plt.show()


sns.countplot(x="survived", data=df, hue="sex")
plt.title("Numbers of survived and gender")
plt.xlabel("survived")
plt.ylabel("count")
plt.show()

sns.boxplot(x="embark_town", y="sex", data=df)
plt.title("Every embark town by sex")
plt.xlabel("Embark Town")
plt.ylabel("Sex")
plt.show()


sns.stripplot(x="sex", y="alive", data=df, jitter=True)
plt.title("Every alive by sex")
plt.xlabel("Sex")
plt.ylabel("Alive")
plt.show()

sns.swarmplot(x="alive", y="embark_town", data=df)
plt.title("Every embark town by alive status")
plt.xlabel("Alive")
plt.ylabel("Embark Town")
plt.show()


sns.jointplot(x="sex", y="class", data=df)
plt.suptitle("Every class by gender",y=1.03)
plt.show()

sns.jointplot(x="age", y="pclass", data=df, kind="kde")
plt.suptitle("Every age by   pclass(Kde)", y=1.03)
plt.show()


sns.pairplot(df[["who", "age", "pclass"]])
plt.suptitle("pairplot - who,age,pclass")
plt.show()


sns.pointplot(x="who", y="alive", data=df, hue="sex")
plt.title("Average Alive by Sex")
plt.xlabel("Sex")
plt.ylabel("Average Alive")
plt.show()


sns.lmplot(x="age", y="alone", data=df)
plt.title("Average Alone by Sex")
plt.xlabel("Sex")
plt.ylabel("Average Alone")
plt.show()
