import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Bu şekilde eksen değerlerini plot methodu ile belirtilir
plt.plot([10, 30, 60, 120], [1, 3, 6, 12])
# xlabel ya da ylabel kullanarak eksenlere etiket verebiliriz
plt.xlabel('yillar')
plt.ylabel('sayilar')
# plt.show()

# 3.argüman renk ve çizgitürünü belirtir
plt.plot([1, 2, 3, 4], [2, 4, 6, 8], 'r')
# axis methodu sırasıyla Xmin,Xmax,Ymin,Ymax değerlerini bir liste olarak alarak görünütlenecek grafik grafik alanın sınırlar...
plt.axis([2, 4, 6, 8])
# plt.show()

# linspace(start,stop,number of samples to generate)
x = np.linspace(0, 5, 6, endpoint=True)
# Bu şekilde birden fazla grafiği bir tabloya koyabilriz
plt.plot(x, x, 'r--', x, x - 2, 'bs', x, x * 5, 'g^')
# plt.show()

x_axis = np.arange(0, 20, 2)
y_axis = x_axis ** 2
plt.plot(x_axis, y_axis, label='linear')
# plt.show()

# np.random.randn(The dimensions of the returned array)
# cumsum : Return the cumulative sum of the elements along a given axis.
# Multiple Plots
fig = plt.figure(figsize=(15, 15))
p1 = fig.add_subplot(2, 2, 1)
plt.plot(np.random.randn(30).cumsum(), "k")
p2 = fig.add_subplot(2, 2, 2)
plt.plot(np.random.randn(100).cumsum(), "k.")
p3 = fig.add_subplot(2, 2, 3)
plt.plot(np.random.randn(50).cumsum(), "k--")
p4 = fig.add_subplot(2, 2, 4)
plt.plot(np.random.randn(50).cumsum(), "k--")
# plt.show()

# numpy.random.randn generates samples from the normal distribution, while
# numpy.random.rand from unifrom (in range [0,1))

# Series: One-dimensional ndarray with axis labels
fig, axes = plt.subplots(2, 1)
data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
data.plot.bar(ax=axes[1], color='r', alpha=0.9)
# plt.show()

raw_data = {'adi': ['Ali', 'Veli', 'Cumali', 'Ayhan', 'Bayhan'],
            'onc_puan': [4, 24, 31, 2, 3],
            'ort_puan': [25, 94, 57, 62, 70],
            'son_puan': [5, 43, 23, 23, 51]}

df = pd.DataFrame(raw_data, columns=['adi', 'onc_puan', 'ort_puan', 'son_puan'])
print(df)

df.plot.hist(bins=10)
# plt.show()

df.hist(column='onc_puan')
# plt.show()
