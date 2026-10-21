import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())

df = sns.load_dataset('flights')
df2 = sns.load_dataset('mpg')
df = df.dropna()
df2 = df2.dropna()

#"SEAICE"
print(df.head())
print(df.shape)
print(df.tail())

print(df.describe(include = 'all'))
print(df.dtypes)
print(df.info())

print(df2.head())
print(df2.shape)
print(df2.tail())

print(df2.describe(include = 'all'))
print(df2.dtypes)
print(df2.info())


print(df.corr(numeric_only = True))
sns.heatmap(df.corr(numeric_only = True), annot = True)
plt.show()


df2.select_dtypes(include = [np.number]).hist(figsize=(12,8))
plt.show()

df.select_dtypes(include = [np.number]).plot(kind = "box",layout = (3,2),sharex = False,sharey = False ,figsize = (8,12))
plt.show()

print(df.month.value_counts())
print(df2.model_year.value_counts())

sns.countplot(x = 'year', data = df)
plt.show()

sns.countplot(x = 'model_year', data = df2)
plt.show()

sns.countplot(x = "mpg",data = df2,hue = "cylinders")
plt.show()

