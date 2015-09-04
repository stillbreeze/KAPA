"""Using the rural.txt corpora in nltk_data. Change the path accordingly at line 21"""

from textblob import TextBlob as tb

def count_words(blob):
	return len(blob.sentences)

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

print ("Sentence Frequency\n")
for i, blob in enumerate(bloblist):
    print("Document {}".format(i + 1))
    print count_words(blob)