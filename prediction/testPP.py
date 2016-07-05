import pickle
from numpy import *
import operator
import numpy

inputString = ['ricorico', 'dog', 'feel']
i = {}

def grabIndex(filename):
	fr = open(filename)
	return pickle.load(fr)
  
def getPreList():  
    for lists in inputString:
       if lists in index:
          i[lists]=index[lists]
    return i

# filename = 'DF_LinearRegression.pickle'
# index = grabIndex(filename)
# getPreList() 
# print filename          
# for key in i:
#     print key 
#     print i[key]

# filename = 'DF_Lasso_0.1.pickle'
# index = grabIndex(filename)
# getPreList() 
# print filename          
# for key in i:
#     print key 
#     print i[key]

filename = 'DF_Lasso_0.9.pickle'
index = grabIndex(filename)
getPreList() 
print filename          
for key in i:
    print key 
    print i[key]

# filename = 'DF_Ridge_0.3.pickle'
# index = grabIndex(filename)
# getPreList() 
# print filename          
# for key in i:
#     print key 
#     print i[key]

# filename = 'DF_Ridge_0.5.pickle'
# index = grabIndex(filename)
# getPreList() 
# print filename          
# for key in i:
#     print key 
#     print i[key]

# filename = 'DF_Ridge_0.99.pickle'
# index = grabIndex(filename)
# getPreList() 
# print filename          
# for key in i:
#     print key 
#     print i[key]

'''
for items in i:
    lastItem = i[items][7]
    lastItem = numpy.asscalar(numpy.float32(lastItem))
    print lastItem
    i[items][7] = lastItem
    print type(i[items][7])
print i
'''
'''
#i = {'ricorico':[1, 0, 0, 0, 0, 0, 0, array([-0.18571429])], 'dog': [25, 39, 25, 25, 25,89, 56, array([22])]}

#thatList = i.get(items)    
'''