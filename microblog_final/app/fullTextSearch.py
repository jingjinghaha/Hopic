import os
import pickle
from numpy import *
import operator


pre = 'index'
input = 'input'
i = {}
outlines = []
scoredOutlines = []
id = 1

def grabIndex(filename):
	fr = open(filename)
	return pickle.load(fr)

def getScoredIndex(id, inputList, index):
   global i, outlines, scoredOutlines
   i = {}
   for list in inputList:
       for word in index:
          if word == list:
	         i[word]=index[word]

   outlines = []
   for item in i.keys():
        for item2 in i[item].keys():
	        outlines.extend([i[item][item2]])

   scoreDic = {}
   for linenumbers in outlines:
       for linenumber in linenumbers:
           scoreDic[linenumber] = 0
   for linenumbers in outlines:
        for linenumber in linenumbers:
            scoreDic[linenumber] += 1

   sorted_scoreDic = sorted(scoreDic.items(), key=operator.itemgetter(1))
   selected_scoreDic = sorted_scoreDic[-3:]
   scoredOutlines = []
   scoredOutlines.extend(x[0] for x in selected_scoreDic)
   return scoredOutlines

def getIdfScoredIndex(id, inputList, index, idfDict):
    global i, outlines, scoredOutlines
    i = {}
    for lists in inputList:
        for word in index:
            if word == lists:
                i[word]=index[word]
                i[word][id].append(idfDict[word])
    outlines = []
    for item in i.keys():
        for item2 in i[item].keys():
	        outlines.extend([i[item][item2]])
    scoreDic = {}
    for linenumbers in outlines:
         for linenumber in linenumbers[0:(len(linenumbers)-1)]:
             scoreDic[linenumber] = 0

    for linenumbers in outlines:
         for linenumber in linenumbers[0:(len(linenumbers)-1)]:
             scoreDic[linenumber] += 1*(linenumbers[-1])

    sorted_scoreDic = sorted(scoreDic.items(), key = operator.itemgetter(1))
    selected_scoreDic = sorted_scoreDic[-3:]
    scoredOutlines = []
    scoredOutlines.extend(x[0] for x in selected_scoreDic)
    return scoredOutlines
'''
    for lists in inputList:
	    if lists in index:
		    i[lists] = index[lists]
		    i[lists][id].append(idfDict[lists])
'''