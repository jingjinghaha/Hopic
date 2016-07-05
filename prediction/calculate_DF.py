import os
import pickle
from numpy import *
import operator
import time


def getFileLens():
	input = 'input'
	len = []
	for i in range(1,9):
		filename = input + str(i)+'.txt'
		fr = open(filename, 'r')
		tmp = 0;
		for i in fr.readlines():
			tmp = tmp +1	
		len.append(tmp)
	return len
def grabIndex(filename):
	fr = open(filename)	
	return pickle.load(fr)
def storeindex(index,filename):
	fw = open(filename,'w')
	pickle.dump(index,fw)
	fw.close()

index1 = grabIndex('index1.pickle')
index2 = grabIndex('index2.pickle')
index3 = grabIndex('index3.pickle')
index4 = grabIndex('index4.pickle')
index5 = grabIndex('index5.pickle')
index6 = grabIndex('index6.pickle')
index7 = grabIndex('index7.pickle')
index8 = grabIndex('index8.pickle')

# tweetnumbers = getFileLens()
# print tweetnumbers

# for key in index1:
# 	# print key
# 	df = len(index1[key])
# 	# print df
# 	value = DF.setdefault(key,[])
# 	value.append(df)

DF = {}
for key in index1:
	# print key
	df = len(index1[key][1])
	value = DF.setdefault(key,[])
	value.append(df)
	# print df
	if key in index2:
		df = len(index2[key][2])
		value.append(df)
	else:
		value.append(0)
		# print df
	if key in index3:
		df = len(index3[key][3])
		value.append(df)
	else:
		value.append(0)
		# print df
	if key in index4:
		df = len(index4[key][4])
		value.append(df)
	else:
		value.append(0)
		# print df
	if key in index5:
		df = len(index5[key][5])
		value.append(df)
	else:
		value.append(0)
		# print df
	if key in index6:
		df = len(index6[key][6])
		value.append(df)
	else:
		value.append(0)
		# print df
	if key in index7:
		df = len(index7[key][7])
		value.append(df)
	else:
		value.append(0)
		# print df
	if key in index8:
		df = len(index8[key][8])
		value.append(df)
	else:
		value.append(0)
		# print df
for key in index2:
	if key not in index1:
		df = len(index2[key][2])
		value = DF.setdefault(key,[])
		value.append(0)
		value.append(df)
		if key in index3:
			df = len(index3[key][3])
			value.append(df)
		else:
			value.append(0)
			# print df
		if key in index4:
			df = len(index4[key][4])
			value.append(df)
		else:
			value.append(0)
			# print df
		if key in index5:
			df = len(index5[key][5])
			value.append(df)
		else:
			value.append(0)
			# print df
		if key in index6:
			df = len(index6[key][6])
			value.append(df)
		else:
			value.append(0)
			# print df
		if key in index7:
			df = len(index7[key][7])
			value.append(df)
		else:
			value.append(0)
			# print df
		if key in index8:
			df = len(index8[key][8])
			value.append(df)
		else:
			value.append(0)
			# print df
for key in index3:
	if key not in index1:
		if key not in index2:
			df = len(index3[key][3])
			value = DF.setdefault(key,[])
			value.append(0)
			value.append(0)
			value.append(df)
			if key in index4:
				df = len(index4[key][4])
				value.append(df)
			else:
				value.append(0)
				# print df
			if key in index5:
				df = len(index5[key][5])
				value.append(df)
			else:
				value.append(0)
				# print df
			if key in index6:
				df = len(index6[key][6])
				value.append(df)
			else:
				value.append(0)
				# print df
			if key in index7:
				df = len(index7[key][7])
				value.append(df)
			else:
				value.append(0)
				# print df
			if key in index8:
				df = len(index8[key][8])
				value.append(df)
			else:
				value.append(0)
				# print df
for key in index4:
	if key not in index1:
		if key not in index2:
			if key not in index3:
				df = len(index4[key][4])
				value = DF.setdefault(key,[])
				value.append(0)
				value.append(0)
				value.append(0)
				value.append(df)
				if key in index5:
					df = len(index5[key][5])
					value.append(df)
				else:
					value.append(0)
					# print df
				if key in index6:
					df = len(index6[key][6])
					value.append(df)
				else:
					value.append(0)
					# print df
				if key in index7:
					df = len(index7[key][7])
					value.append(df)
				else:
					value.append(0)
					# print df
				if key in index8:
					df = len(index8[key][8])
					value.append(df)
				else:
					value.append(0)
					# print df
for key in index5:
	if key not in index1:
		if key not in index2:
			if key not in index3:
				if key not in index4:
					df = len(index5[key][5])
					value = DF.setdefault(key,[])
					value.append(0)
					value.append(0)
					value.append(0)
					value.append(0)
					value.append(df)
					if key in index6:
						df = len(index6[key][6])
						value.append(df)
					else:
						value.append(0)
						# print df
					if key in index7:
						df = len(index7[key][7])
						value.append(df)
					else:
						value.append(0)
						# print df
					if key in index8:
						df = len(index8[key][8])
						value.append(df)
					else:
						value.append(0)
						# print df
for key in index6:
	if key not in index1:
		if key not in index2:
			if key not in index3:
				if key not in index4:
					if key not in index5:
						df = len(index6[key][6])
						value = DF.setdefault(key,[])
						value.append(0)
						value.append(0)
						value.append(0)
						value.append(0)
						value.append(0)
						value.append(df)
						if key in index7:
							df = len(index7[key][7])
							value.append(df)
						else:
							value.append(0)
							# print df
						if key in index8:
							df = len(index8[key][8])
							value.append(df)
						else:
							value.append(0)
							# print df
for key in index7:
	if key not in index1:
		if key not in index2:
			if key not in index3:
				if key not in index4:
					if key not in index5:
						if key not in index6:
							df = len(index7[key][7])
							value = DF.setdefault(key,[])
							value.append(0)
							value.append(0)
							value.append(0)
							value.append(0)
							value.append(0)
							value.append(0)
							value.append(df)
							if key in index8:
								df = len(index8[key][8])
								value.append(df)
							else:
								value.append(0)
								# print df
for key in index8:
	if key not in index1:
		if key not in index2:
			if key not in index3:
				if key not in index4:
					if key not in index5:
						if key not in index6:
							if key not in index7:
								df = len(index8[key][8])
								value = DF.setdefault(key,[])
								value.append(0)
								value.append(0)
								value.append(0)
								value.append(0)
								value.append(0)
								value.append(0)
								value.append(0)
								value.append(df)
								# print df
storeindex(DF,'DF.pickle')
