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

for l in listtext:
    for word in l.split(" "):
        words.append(word)

print("Using Lemmatization:")
lemmatizer = WordNetLemmatizer()
print[lemmatizer.lemmatize(word) for word in words]

print("Using POS:")
a=pos_tag(words)
for word in a:
    if 'VB' in word[1]:
        words.remove(word[0])
print(words)


wordsnew=words
listfr=[]
listtop=[]
for i in words:
    num=0
    for j in wordsnew:
        if i==j:
            num=num+1
    if (num,i) not in listfr:
        listfr.append((num,i))
listfr.sort()
print("Quantity of remaining words:")
print(listfr)
print("Top five words:")
for i in range(5):
    listtop.append(listfr[i-5][1])
    print(listfr[i-5])

for i in listtop:
    for j in listtext:
        if i in j:
             print(j)









