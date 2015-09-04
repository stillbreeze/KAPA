"""Interpolated N-gram document frequency - INDF"""


from __future__ import division
import math
from textblob import TextBlob as tb

#calculates number of documents containing a word
def n_containing1(word, bloblist):
    return sum(1 for blob in bloblist if word[0] in blob)

#calculates number of documents containing a word
def n_containing2(word, bloblist):
    return sum(1 for i in range(0,len(bloblist)-1) if word[0] in bloblist[i] and word[1] in bloblist[i+1])

#returns a list of sentences
def make_sentences(bloblist):
	return bloblist.sentences

#calculates average unigram document frequency for a sentence
def df_unigram(sentence,bloblist):
    tot=sum(n_containing1(word,bloblist)/len(bloblist) for word in sentence.ngrams(n=1))
    return tot/len(sentence)

#calculates average bigram document frequency for a sentence
def df_bigram(sentence,bloblist):
    tot=sum(n_containing2(word,bloblist)/len(bloblist) for word in sentence.ngrams(n=2))
    return tot/len(sentence)

#calculates a weighted linear combination of unigrams and bigrams
def indf(bloblist,alpha):
    for i, blob in enumerate(bloblist):
        sentences=make_sentences(blob)
        print ("Document {}".format(i+1))
        for j, sentence in enumerate(sentences):
            dfug=df_unigram(sentence,bloblist)
            dfbg=df_bigram(sentence,bloblist)
            print ("Sentence {}".format(j+1))
            print ((alpha*dfug) + ((1-alpha)*dfbg))/len(sentence)
        print "\n\n"


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

indf(bloblist,alpha)