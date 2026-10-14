
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
df = df.dropna()

sns.barplot(x ="day",y = "total_bill",data = df,  hue = "sex")
plt.title("Total Bill by Day and Sex")
plt.xlabel("Days of the week")
plt.ylabel("Average Bills")
plt.show()


sns.countplot(x = "day",data = df,hue = "sex")
plt.title("Numbers of diners by day and gender")
plt.xlabel("Days of the week")
plt.ylabel("Number of Diners")
plt.show()

sns.boxplot(x = "day",y = "total_bill",data = df)
plt.title("Every bill amount Per  day")
plt.xlabel("Days of the week ")
plt.ylabel("Bills")
plt.show()


sns.stripplot(x = "day",y = "total_bill",data = df, jitter = True)
plt.title("Every bill amount Per  day")
plt.xlabel("Days of the week ")
plt.ylabel("Bills")
plt.show()

sns.swarmplot(x = "day",y = "total_bill",data = df)
plt.title("Every bill amount Per  day")
plt.xlabel("Days of the week ")
plt.ylabel("Bills")
plt.show()


sns.jointplot(x = "total_bill",y = "tip",data = df)
plt.suptitle("Total Bill vs Tips", y=1.03)
plt.show()

sns.jointplot(x = "total_bill",y = "tip",data = df,kind = "kde")
plt.suptitle("Total Bill vs Tips (kde)", y=1.03)
plt.show()

sns.pairplot(df[["total_bill","tip","size"]])
plt.suptitle("Pairplot - Total Bill, Tips and Size")
plt.show()


sns.pointplot(x = "day",y = "total_bill",data = df, hue = "sex")
plt.title("Total Bill by Day and Sex")
plt.xlabel("Days of the week")
plt.ylabel("Average Bills")
plt.show()


sns.lmplot(x = "tip",y = "total_bill",data = df)
plt.title("Total Bill vs tip")
plt.xlabel("Tips")
plt.ylabel("Total Bill")
plt.show()