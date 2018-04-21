import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/justmarkham/python-data-analysis-workshop/master/drinks.csv"
drinks = pd.read_csv(url)
print(drinks.head(6))
print(drinks.tail(5))

print(drinks.describe())
print(drinks.info())

# Veride eksik değerler var mı?
print(drinks.isnull().sum())

# .iloc to explicity support only integer indexing, and
# .loc to explicity support only label indexing
print(drinks.loc[[5]])
# Eksik verileri 'NA' ile doldurduk
# dropna() on a DataFrame will REMOVE every row that has at least one NaN or NULL value in it.
# fillna()will FILL these NaN or NULL values with some value provided to the function.
drinks.dropna()
drinks = drinks.fillna(value="NA")
print(drinks.iloc[[5]])

drinks['toplam_hizmet'] = drinks.wine_servings + drinks.spirit_servings + drinks.beer_servings
print(drinks.head(5))

# şarap servisi 300'den yukarı
print(drinks[drinks['wine_servings'] > 300].count())

print(drinks[drinks['wine_servings'] > drinks['beer_servings']].head())

# avrupa kıtasının bira servis ortalamasını bulun
print(drinks[drinks.continent == 'EU'].beer_servings.mean())

# avrupa kıtasının bira servis ortalamasını bulun
print(drinks.groupby('continent').beer_servings.mean())

print(drinks.groupby('continent').toplam_hizmet.max())

# Her kıtadaki ülkelerin sayısını görselleştirin bar plot
drinks.continent.value_counts().plot(kind='bar', title='Ulke Sayilari')
plt.xlabel('Kita')
plt.ylabel('Sayi')
# plt.show()

# Kıtaların bira ortalamalarını bar plot ile görselleştirin
drinks.groupby('continent').beer_servings.mean().plot(kind='bar', title='Kitalarin Bira Ortalamasi')
# plt.show()

drinks.beer_servings.hist(bins=10)
# plt.show()
# plt.savefig('beer_histogram.png')

# bira servisini kıtalara göre gruplandırarak histogramla görselleştirin
drinks.beer_servings.hist(by=drinks.continent, bins=10)
# plt.show()

# scatterplot ile bira ve şarap servislerini karşılatırın
drinks.plot(x="beer_servings", y="wine_servings", kind="scatter", alpha=0.3, c="r")
plt.show()

# aynı scatterplot ancak Avrupa ülkeleri dışındakiler kırmızı kalsın
colors = np.where(drinks.continent == 'EU', 'r', 'b')
print(colors)

drinks.plot(x="beer_servings", y="wine_servings", kind="scatter", c=colors)
plt.show()

drinks.beer_servings.plot(kind='hist', bins=20, title='Histogram of Beer Servings')
plt.xlabel('Beer Servings')
plt.ylabel('Frequency')
plt.savefig('beer_histogram.png')