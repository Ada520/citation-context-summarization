import sys
import re
import os
from nltk import word_tokenize
from nltk.util import bigrams


bigramsDF = {}

for f in os.listdir('../contextFiles/'):
	
	originalSents = []
	sents = []
	

	with open('../contextFiles/' + f) as inputFile:
		inputLines = [x.decode('utf-8',"replace").strip('\n').lower() for x in inputFile.readlines()]
		sentId = 0
		for line in inputLines:
			originalSents.append(line)
			#print line
			line = re.sub(r'\([^\)]*\)', '', line)
			line = re.sub(r'\[[^\]]*\]', '', line)
			line = re.sub(r'\s+', ' ', line)
			sents.append(line)
			sentId = sentId + 1

		documentTokens = []
		
		for line in sents:
			tokens = word_tokenize(line)
			bigramsSet = list(bigrams(tokens))
			documentTokens.extend(bigramsSet)

		documentTokens = set(list(documentTokens))

		for token in documentTokens:
			if (token[0] + " " + token[1]) not in bigramsDF:
				bigramsDF[token[0] + " " + token[1]] = 1
			else:
				bigramsDF[token[0] + " " + token[1]] = bigramsDF[token[0] + " " + token[1]] + 1
				


with open('../IDFMetrics/BgIdf.txt', 'w') as output:
	for bigram in bigramsDF:
		output.write(bigram.encode('utf-8') + "\t" + str(bigramsDF[bigram]) + "\n")
			



