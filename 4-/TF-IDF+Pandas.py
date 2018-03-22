import os
import numpy as np
import pandas as pd
import string


# You can use the maketrans() helper function in the string module to create a translation table.
# The method translate() returns a copy of the string in which all characters have been translated using table (constructed with the maketrans() function in the string module), optionally deleting all characters found in the string deletechars.
def removePunctuation(line):
    table = str.maketrans({key: None for key in string.punctuation})
    translation = line.translate(table)
    return translation


docsize = 0
folder = 'people/'
documents = []
allwords = []
# The method listdir() returns a list containing the names of the entries in the directory given by path
for fn in os.listdir(folder):
    if fn.endswith('.txt'):
        f = open(folder + fn, 'r', encoding='utf8')
        documents.append(folder + fn)
        for line in f:
            line = line.lower()
            translation = removePunctuation(line)
            words = translation.split()
            allwords.extend(words)
        docsize += 1

print(len(allwords))
vocabulary = list(set(allwords))
vocsize = len(vocabulary)

termfreq = np.zeros((vocsize, docsize))
print('Doc size', docsize, ' Vocabulary size', vocsize)

for i in range(docsize):
    allwords = []
    f = open(documents[i], 'r', encoding='utf8')
    for line in f:
        line = line.lower()
        translation = removePunctuation(line)
        words = translation.split()
        allwords.extend(words)
    for k in range(len(vocabulary)):
        freq = allwords.count(vocabulary[k])
        termfreq[k, i] = freq

print(termfreq.shape)

tdf_idf_pd = pd.DataFrame(termfreq, columns=documents, index=vocabulary)
print(tdf_idf_pd.head())

print(tdf_idf_pd['people/DonaldTrump.txt'].sort_values(ascending=False))
