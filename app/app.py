import os
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

path = '/home/azhd/Documents/Projects/vika-topmodeling'
# print(path)
list_files = [f for f in os.listdir(path) if f.endswith('.txt')]
stopWords = set(stopwords.words('russian'))
# stopWords = ['и', 'в']

stemmer = SnowballStemmer("russian")

words = {}

for f in list_files:
    txt_file = open(path + '/' + f, 'r')
    txt_array = txt_file.read().replace("\n", "").split(" ")
    txt_stemm_array = [stemmer.stem(word) for word in txt_array]
    wordsFiltered = []
    for w in txt_stemm_array:
        if w not in stopWords:
            wordsFiltered.append(w)
            words[f] = wordsFiltered
print(words)