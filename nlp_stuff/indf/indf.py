"""Interpolated N-gram document frequency - INDF"""


from __future__ import division
import math
from textblob import TextBlob as tb

#calculates number of documents containing a word
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

#returns a list of sentences
def make_sentences(bloblist):
	return bloblist.sentences

#calculates average unigram document frequency for a sentence
def df_unigram(sentence,bloblist):
    tot=sum(n_containing(word,bloblist)/len(bloblist) for word in sentence.words)
    return tot/len(sentence)

#calculates average bigram document frequency for a sentence
#def df_bigram(sentence,bloblist):


#calculates a weighted linear combination of unigrams and bigrams
def indf(bloblist):
    for blob in bloblist:
        sentences=make_sentences(blob)
        for sentence in sentences:
            dfug=df_unigram(sentence,bloblist)
            print dfug
            print "\t"
        print "\n"
#           dfbg=df_bigram(sentence,bloblist)

#builds a list of documents
def make_bloblist(bloblist):
    f = open('/home/ashar/nltk_data/corpora/abc/rural.txt','r')
    var = f.read()
    var = var.lower()
    splat=var.split("\n\n")
    for i in splat:
        temp=tb(i.decode('utf-8'))
        bloblist.append(temp)


#the weight distribution factor between unigram and bigram
alpha = 0.3

bloblist = []
make_bloblist(bloblist)

indf(bloblist)