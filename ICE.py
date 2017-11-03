import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk import ne_chunk
from nltk.util import ngrams
from collections import Counter
import random

file = open("test.txt")

listtext=[]
list=[]
words=[]
line = file.readline()
i=random.randint(1, 10)
while(line):
    listtext.append(line)
    line = file.readline()


for i in range(i,i+3):
    list.append(listtext[i])

print("Using wordNet:")
for l in list:
    for word in l.split(" "):
        words.append(word)
        word_synsets = wn.synsets(word)
        print[str(syns.definition) for syns in word_synsets]

print("Using tokenization:")
for l in list:
    print[sent_tokenize(l)]

print("Using stemming(Lancaster):")  #run
stemmer = LancasterStemmer()
print [stemmer.stem(word) for word in words]


print("Using POS:")
print pos_tag(words)

print("Using Lemmatization:")   #runing
lemmatizer = WordNetLemmatizer()
print[lemmatizer.lemmatize(word) for word in words]


print("Using Trigram:")
for l in list:
    n=nltk.word_tokenize(l)
    grams = ngrams(n, 3)
    print Counter(grams)


print("Using Named Entity Recognition:")
for l in list:
    print ne_chunk(pos_tag(wordpunct_tokenize(l)))