from __future__ import division
import nltk
from textblob import TextBlob as tb

inputdoc = open("/home/ashar/nltk_data/corpora/abc/rural.txt")
data = inputdoc.read()
# Break down into documents
paragraphs = data.split("\n\n")

for number,paragraph in enumerate(paragraphs):
	print "Paragraph no. {}".format(number + 1)
	for num,line in enumerate(paragraph.split("\n")):
		print "Line no. {}".format(num + 1)
		# Processing here
		text = nltk.word_tokenize(line)
		# POS tagging
		pos_text = nltk.pos_tag(text)
		# Dictionary for holding sentence data
		freq_dict = {}
		# No of words in sentence
		count = 0
		# Make dictionary for POS frequency
		for tagged_word in pos_text:
			freq_dict[tagged_word[1]] = freq_dict.get(tagged_word[1], 0) + 1
			count += 1
		# Normalise data
		for entry in freq_dict:
			freq_dict[entry]/=count
		print freq_dict

