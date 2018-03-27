import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv')
print(df.head())

# Concise summary of a DataFrame.
df.info()
# Generates descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s
# distribution, excluding NaN values
print(df.describe())

print(df[df.Age.isnull()].head())

df_temp = df[df.Age.notnull()]
print(df_temp.Sex.value_counts())

# to show up automatically without stopping execution, turn on interactive mode with plt.ion()
plt.ion()
# df_temp.Sex.value_counts().plot(kind='bar')

# df.Age.value_counts().plot(kind='bar')
# df.Age.hist(bins=10)
# plt.show()

aliveCustomers = df[df.Survived == 1]
print(aliveCustomers)

aliveCustomersGroupingByClass = df[df.Survived == 1].groupby('Pclass').count()
print(aliveCustomersGroupingByClass)

aliveCustomersGroupingByClass2 = df[df.Survived == 1].groupby('Pclass').Survived.value_counts()
print(aliveCustomersGroupingByClass2)
# df[df.Survived == 1].groupby('Pclass').Survived.value_counts().plot(kind='bar')

aliveCustomersGroupingByClassAndAvearageCosts = df[df.Survived == 1].groupby('Pclass').Fare.mean()
print(aliveCustomersGroupingByClassAndAvearageCosts)

allCustomersGroupingByClassAndAvearageCosts = df.groupby('Pclass').Fare.mean()
print(allCustomersGroupingByClassAndAvearageCosts)

aliveCustomersGroupingByClassAndSexStats = df[df.Survived == 1].groupby('Pclass').Sex.value_counts()
print(aliveCustomersGroupingByClassAndSexStats)
# aliveCustomersGroupingByClassAndSexStats.plot(kind='bar')


deadAndHasRelatives = df[(df.Survived == 0) & ((df.SibSp > 0) | (df.Parch > 0))]
print(deadAndHasRelatives.head())

deadAndHasRelativesGroupingByClass = deadAndHasRelatives.groupby('Pclass').Survived.count()
print(deadAndHasRelativesGroupingByClass)
#deadAndHasRelativesGroupingByClass.plot(kind='bar')
