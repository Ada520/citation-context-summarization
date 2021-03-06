import sys
import math
import re

def getIDFs():
	with open("idf.txt","r") as idfFile:
		idf = {}
		N = 0

		for line in idfFile:
			line = line.rstrip().split('\t')
			tok = line[0]
			idf[tok] = int(line[1])
			N = N + idf[tok]

		print N
		for token in idf:
			idf[token] = math.log(N/(1+float(idf[token])))

		return idf
		
		


def getLexSim(sent1, sent2):
	
	count1 = {}
	count2 = {}

	wordSet1 = re.split("\W+", sent1)
	
	for word in wordSet1:
		if word in count1:
			count1[word] = count1[word] + 1
		else:
			count1[word] = 1

	wordSet2 = re.split("\W+", sent2)

	for word in wordSet2:
		if word in count2:
			count2[word] = count2[word] + 1
		else:
			count2[word] = 1
	
	
	wordsList = list(set(wordSet1 + wordSet2))
	wordsList.sort()
	

	c1 = 0
	c2 = 0
	idf = 0
	c = 0
	rs1 = 0
	rs2 = 0

	countC = {}

	for word in wordsList:
		if word in count1:
			c1 = count1[word]
		else:
			c1 = 0

		if word in count2:
			c2 = count2[word]
		else:
			c2 = 0


		if word in idfDict:
			idf = idfDict[word]
		else:	
			idf = 1
		c1 = c1 * idf
		c2 = c2 * idf
	
		c = c + c1*c2

		countC[word] = c1*c2
		
		rs1 = rs1 + c1*c1
		rs2 = rs2 + c2*c2

#	keys = sorted(countC, key = lambda token : countC[token], reverse = True)

#	for key in keys:
		
	r = math.sqrt( rs1 * rs2)
	
	if (r == 0):
		return 0
	else:
		return c/r





inputFile =  open("outputs/tempSents.txt")

inputLines = {}

for line in inputFile:
	inputLines[int(line.split("\t")[0])] = 	line.split("\t")[1].decode('utf-8').strip('\n').lower()
#inputLines = [x.decode('utf-8').strip('\n').lower() for x in inputFile.readlines()]
#sentId = 0
idfDict = getIDFs()

sims = open("outputs/sims.txt", "w")
for sent1 in inputLines:
	for sent2 in inputLines:
		sims.write(str(sent1) + "\t" + str(sent2) + "\t" + str(getLexSim(inputLines[sent1], inputLines[sent2])) + "\n")

#sims.write("\n\n\n\n")
#for sent in inputLines:
#	sims.write(str(sent) + "\t" + inputLines[sent].encode('utf-8') + "\n")

		
	

