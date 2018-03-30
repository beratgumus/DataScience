import pandas as pd
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
# deadAndHasRelativesGroupingByClass.plot(kind='bar')

deadGroupingByclass = df[df.Survived == 0].groupby('Pclass').PassengerId.count()
print(deadGroupingByclass)

# # Gemideki kurtulamayan ve dışarda akrabaları olan kişilerin, kurtulamayanlar arasındaki siniflara gore oransal
# dağılımı için
percentange = deadAndHasRelativesGroupingByClass / deadGroupingByclass
print(percentange)
# percentange.plot(kind ='bar')

#  pd.cut: Return indices of half-open bins to which each value of x belongs.
age_bin = [0, 18, 25, 40, 60, 100]
ageIntervalAsSeries = pd.cut(df.Age, bins=age_bin)
print(ageIntervalAsSeries.head())

# bu yaş aralık serisini yeni bir sütun olarak ekler
df['AgeBin'] = ageIntervalAsSeries
print(df.head())

df_AgeWithoutNull = df[df.Age.notnull()]
# Hayata kalan kişilerin yaş aralıklarına göre sayısını bulmak için
aliveGroupingByAgeInterval = df_AgeWithoutNull.groupby('AgeBin').Survived.sum()
print(aliveGroupingByAgeInterval)
aliveGroupingByAgeInterval.plot(kind='pie')
