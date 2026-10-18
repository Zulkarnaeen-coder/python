import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())

df = sns.load_dataset('planets')
df = df.dropna()
print(df.head())
print(df.shape)
print(df.tail())
print(df.describe(include = 'all'))
print(df.dtypes)
print(df.info())

print(df.corr(numeric_only = True))
sns.heatmap(df.corr(numeric_only = True), annot = True)
plt.show()


df.select_dtypes(include = [np.number]).hist(figsize=(12,8))
plt.show()

df.select_dtypes(include = [np.number]).plot(kind = "box",layout = (3,2),sharex = False,sharey = False ,figsize = (8,12))
plt.show()


print(df.mass.value_counts())
print(df.year.value_counts())

sns.countplot(x = 'year', data = df)
plt.show()

sns.countplot(x = "mass",data = df,hue = "method")
plt.show()

sns.pairplot(df,x = "mass", hue = "method")
plt.show()