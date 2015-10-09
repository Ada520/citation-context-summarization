import os
import sys

# python createFactMatrix.py <factMatrixFolderName> <contextFolder> <summary/n>

for filename in os.listdir("../"+sys.argv[2] + '/'):
		fact_list = {}
		output = open("../"+sys.argv[1] + '/'+filename,'w')
		if (sys.argv[3] == 'summary'):
			fact_file = open('../facts/'+filename[:-9]+'.ann','r')
		else:
			fact_file = open('../facts/'+filename[:-3]+'ann','r')			
		for line in fact_file:
			print line
			line = line.rstrip().split('\t')
			fact_id  = int(line[0])
			if fact_id not in fact_list:
				fact_list[fact_id] = []
				fact_list[fact_id].append(line[1])
			else:
				fact_list[fact_id].append(line[1])
		
		context_file = open("../"+sys.argv[2] + '/'+filename,'r')
		for line in context_file:
			for key in fact_list:
				present = 0
				for fact in fact_list[key]:
					if fact in line:
						output.write('1'+'\t')
						present = 1
						break
				if present == 0:
					output.write('0'+'\t')
			output.write('\n')
		print  fact_list
