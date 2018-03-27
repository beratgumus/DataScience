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
df_temp.Sex.value_counts().plot(kind='bar')

df.Age.value_counts().plot(kind='bar')
#print(df.Age.hist(bins=10))