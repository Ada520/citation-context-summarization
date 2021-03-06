import os
import sys

#python createPyramid.py <factWeightsFolder> <factPyramidFolder>

for filename in os.listdir("../"+sys.argv[1] + '/'):
		output = open("../"+sys.argv[2] +  '/'+filename,'w')
		print filename
		fact_matrix_file = open("../"+sys.argv[1] + '/'+filename,'r')
		weight = {}
		for line in fact_matrix_file:
			line = map(int,line.rstrip().split('\t'))
			i = line[1]
			j = line[0]
			if i  not in weight:
				weight[i] = []
				weight[i].append(j)
			else:
				weight[i].append(j)
		
		
		for w in weight:
			print w, weight[w]

		for w in list(reversed(sorted(weight.keys()))):
			fact_list = ",".join(map(str,weight[w]))
			output.write(str(w)+'\t'+fact_list+'\n')
