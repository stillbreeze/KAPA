from textblob import TextBlob as tb

inputdoc = open("rural.txt")
data = inputdoc.read()
# Break down into documents
paragraphs = data.split("\n\n")

for number,paragraph in enumerate(paragraphs):
	print "Paragraph no. {}".format(number + 1)
	for num,line in enumerate(paragraph.split("\n")):
		print "Line no. {}".format(num + 1)
		line_input = tb(line)
		print line_input.sentiment
		