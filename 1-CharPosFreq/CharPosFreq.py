import string
from math import *

harf_pos_freq = {}
f = open('haber.txt', 'r')
maxLen = 30

for line in f:
    words = line.lower().strip().split()
    for word in words:
        word = ''.join([ch for ch in word if ch not in string.punctuation])
        if len(word) <= maxLen:
            for i in range(len(word)):
                if word[i] not in harf_pos_freq:
                    harf_pos_freq[word[i]] = [0] * 30
                harf_pos_freq[word[i]][i] += 1


# for k in sorted(harf_pos_freq):
# print(k,':',harf_pos_freq[k],'toplam:',sum(harf_pos_freq[k]))


def square_rooted(x):
    return round(sqrt(sum([a * a for a in x])), 3)


def cosine_similarity(x, y):
    numerator = sum(a * b for a, b in zip(x, y))
    denominator = square_rooted(x) * square_rooted(y)
    return round(numerator / float(denominator), 3)


def getSimilarity(x, y):
    return similarity[x][y]


def getMaxSimilar():
    max = 0.0
    for i in similarity:
        for j in similarity:
            value = similarity[i][j]
            if value > max and value != 1:
                a, b, max = i, j, value

    return a, b, max


similarity = {}
for i in sorted(harf_pos_freq):
    similarity[i] = {}
    for j in sorted(harf_pos_freq):
        result = cosine_similarity(harf_pos_freq[i], harf_pos_freq[j])
        similarity[i][j] = result

for k in sorted(similarity):
    print(k, ':', similarity[k])

char1 = 'a'
char2 = 'b'
if getSimilarity(char1, char2) == getSimilarity(char2, char1):
    print('IT IS WORKINGGG!!!')

print(getMaxSimilar())

