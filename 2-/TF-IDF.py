import numpy as np
import math

docsize = 5
vocabulary = ['yapay','zekâ','zeki','mobil','ekonomi','yeni','euro','dolar','faiz','büyüme']

vocsize =len(vocabulary)
termfreq = np.zeros((vocsize, docsize))

for i in range(docsize):
    allwords = []
    f = open("haber" + str(i) + '.txt', 'r', encoding="utf8")
    for line in f:
        words = line.lower().strip().split()
        allwords.extend(words)
    for k in range(len(vocabulary)):
        freq = allwords.count(vocabulary[k])
        termfreq[k, i] =freq

#print(termfreq)

math.log(float(5)/3) # bir kelime 5 tane döküman arasında 3 tanesi geçiyorsa idf skoru

