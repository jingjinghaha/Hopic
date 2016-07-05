import pickle
from numpy import *
from kmeans import *
import dbscan,operator
def grabIndex(filename):
	fr = open(filename)	
	return pickle.load(fr)
	
def getFileLens():
	input = 'input'
	len = []
	for i in range(1,8):
		filename = input + str(i)+'.txt'
		fr = open(filename, 'r')
		tmp = 0;
		for i in fr.readlines():
			tmp = tmp +1	
		len.append(tmp)
	return len
	
def getFileLen(id):
	input = 'input'
	filename = input + str(id)+'.txt'
	fr = open(filename, 'r')
	tmp = 0;
	for i in fr.readlines():
		tmp = tmp +1	
	return tmp
	
	
def dense_vectorize(index,id):
	print 'id is: ' ,id
	termNum = len(index)
	tweetNum = getFileLen(id)
	#lenList = getFileLens()
	#tweetNum = sum(lenList)
	#tweetNum = lenList[0]
	print ((termNum,tweetNum))
	mat = zeros((termNum,tweetNum))
	termList = []
	axis = -1
	for item in index:
		axis = axis+1
		termList.append(item)
		subDit =  index[item]
		for docId in subDit:
			postlist = subDit[docId]
			for line in postlist:
				#absolute_tweet = sum(lenList[:id-1]) + line
				absolute_tweet = line - 1
				mat[axis,absolute_tweet] += 1
	return termList,mat
	
def sparse_Vectorize(index,id):
	print 'id is: ' ,id
	termNum = len(index)
	tweetNum = getFileLen(id)
	print ((termNum,tweetNum))
	termList = []
	matrix = {}
	axis = -1
	for item in index:
		axis = axis + 1
		termList.append(item)
		subDit = index[item]
		for docId in subDit:
			postlist = subDit[docId]
			for line in postlist:
				key = line
				positionList = matrix.setdefault(key,[])
				positionList.append(axis)
	matrix['len'] = termNum
	return termList,matrix

def sparse_process_dbscan(id):
	pre = 'index' 
	filename = pre+str(id)+'.pickle'
	index = grabIndex(filename)
	termList, mat = sparse_Vectorize(index,id)
	outputFileName = 'outputSparseMatrix' + str(id) + '.txt'
	fw = open(outputFileName, 'w')
	for key in mat:
		fw.write(str(key)+": ")
		fw.write(str(mat[key]))
		fw.write('\n')
	fw.close()
	#center,cluster = kMeans_Sparse(mat,k)
	#center,cluster = miniBatch_KMeans_Sparse(mat,k,100,100)
	#print center,cluster
	clusterResult = dbscan.sparse_dbscan(mat,0.9,15)
	print "finish dbscan....."
	print "len of cluster:", len(clusterResult)
	print "Generating cluster files......"
	for key in clusterResult:
		fwritefile = open('filecluster'+str(key)+'.txt','w')
		fr2 = open('input'+str(id)+'.txt','r')
		linecnt = 0
		for ss in fr2.readlines():
			linecnt = linecnt+ 1
			if linecnt in clusterResult[key]:
				print >>fwritefile,ss
		fr2.close()
		fwritefile.close()
	print "Generating cluster info......"
	labelInfo = {}
	fw = open("DBSCAN_Res"+str(id)+".txt",'w')
	fwlabel = open("DBSCAN_Res"+str(id)+'label.txt','w')
	for key in clusterResult:
		labelInfo.setdefault(key,{})
		for i in clusterResult[key]:
			includedTerms = mat[i]
			for term in includedTerms:
				cnt = labelInfo[key].setdefault(term,0)+1
				labelInfo[key][term] = cnt
		b = sorted(labelInfo[key].iteritems(),key=operator.itemgetter(1),reverse=True)
		#print type(b[0][0]),b[1][0]
		fw.write("Cluster %-10s:" % key)
		for i in range(len(clusterResult[key])):
			fw.write("%-10s"%clusterResult[key][i])
		fw.write('\n')
		if len(b)>1:
			label = (termList[b[0][0]],termList[b[1][0]])
			fwlabel.write("%-10s"%('label '+str(key)+':',))
			fwlabel.write(' '+str(label[0])+' '+str(label[1]))
		else:
			label = (termList[b[0][0]],)
			fwlabel.write("%-10s"%('label '+str(key)+":",))
			fwlabel.write(' '+str(label[0]))
		fwlabel.write('\n')
		
	fwlabel.close()
	fw.close()
	# print center 
	# for i in range(shape(cluster)[0]):
		# print cluster[i,0],cluster[i,1]
	
				
			
def dense_process(id):
	pre = 'index' 
	filename = pre+str(id)+'.pickle'
	index = grabIndex(filename)
	termList, mat = vectorize(index,id)
	outputFileName = 'outputMatrix' + str(id) + '.txt'
	fw = open(outputFileName, 'w')
	for i in range(len(termList)):
		fw.write("%-50s"%termList[i])
		fw.write('\t')
		for j in range(shape(mat)[1]):
			fw.write(str(int(mat[i,j])))
			fw.write('\t')
		fw.write('\n')
	fw.close()
	center,cluster = kMeans_Sparse(mat,7)
	print center,cluster

#process(9)		
sparse_process_dbscan(9)
#print getFileLens()