"""Using the rural.txt corpora in nltk_data. Change the path accordingly at line 21"""

from __future__ import division
import math
from textblob import TextBlob as tb

#calculates normalized term frequency
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

#calculates number of documents containing a word
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

#calculates the inverse document frequency
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

#calculates the final score for each word
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

#calcualates the score for each sentence
#def sent_score():

#builds a list of documents
def make_bloblist(bloblist):
    f = open('/home/ashar/nltk_data/corpora/abc/rural.txt','r')
    var = f.read()
    var = var.lower()
    splat=var.split("\n\n")
    for i in splat:
        temp=tb(i.decode('utf-8'))
        bloblist.append(temp)

bloblist = []
make_bloblist(bloblist)

for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[-15:]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

