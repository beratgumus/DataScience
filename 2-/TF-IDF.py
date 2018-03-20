import numpy as np
import math

docsize = 5
vocabulary = ['yapay', 'zekâ', 'zeki', 'mobil', 'ekonomi', 'yeni', 'euro', 'dolar', 'faiz', 'büyüme']

vocsize = len(vocabulary)
termfreq = np.zeros((vocsize, docsize))  # creates an array full of zeros

for i in range(docsize):
    allwords = []
    f = open("haber" + str(i) + '.txt', 'r', encoding="utf8")
    for line in f:
        words = line.lower().strip().split()
        allwords.extend(words)
    for k in range(len(vocabulary)):
        freq = allwords.count(vocabulary[k])
        termfreq[k, i] = freq


# print(termfreq)

# math.log(float(5)/3)    # bir kelime 5 tane döküman arasında 3 tanesi geçiyorsa idf skoru


def idf(termfreq, term_index):
    _, n_doc = termfreq.shape  # the dimensions of the array, n rows and m columns, shape will be (n,m).
    df = np.count_nonzero(termfreq[term_index, :])  # Counts the number of non-zero values in the array
    return math.log(float(n_doc) / df)


invdfreq = np.zeros((vocsize, 1))

for index in range(vocsize):
    invdfreq[index, 0] = idf(termfreq, index)

# print(invdfreq)

tf_idf = termfreq * invdfreq


# print(tf_idf)


def l2_norm(a):
    return math.sqrt(np.dot(a, a))


def cosine_similiarity(a, b):
    return np.dot(a, b) / (l2_norm(a) * l2_norm(b))


a = np.arange(10)  # arrange(start,stop,step)
b = np.ones(10)  # ones creates an array full of ones


# print(np.dot(a,b))  #inner product of vectors


def doc_similarity(tf_idf, doc1, doc2):
    return cosine_similiarity(tf_idf[:, doc1], tf_idf[:, doc2])


print(doc_similarity(tf_idf, 0, 4))
print(doc_similarity(tf_idf, 0, 1))


def term_similarity(tf_idf, term1, term2):
    return cosine_similiarity(tf_idf[term1, :], tf_idf[term2, :])


print(term_similarity(tf_idf, 0, 1))
print(term_similarity(tf_idf, 0, 4))

print(term_similarity(tf_idf, vocabulary.index('dolar'), vocabulary.index('euro')))
print(term_similarity(tf_idf, vocabulary.index('zekâ'), vocabulary.index('yapay')))
