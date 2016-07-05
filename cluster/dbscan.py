#import ddbscan
#import matplotlib
#import matplotlib.pyplot as plt
from numpy import *
#from sklearn.cluster import DBSCAN
def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat
	
# def distEclud(vecA, vecB):
    # return sqrt(sum(power(vecA - vecB, 2))) #la.norm(vecA-vecB)
	
# def demo_DBSCAN():
	# data = loadDataSet('testSet.txt')
	# arrayData = array(data)
	# dbscan = DBSCAN(1.2,6)
	# dbscan.fit(arrayData)
	# fig  = plt.figure()
	# ax = fig.add_subplot(121)
	# ax.scatter(array(data)[:,0],array(data)[:,1],c=dbscan.labels_)
	# #ax1 = fig.add_subplot(122)
	# #ax1.scatter(array(dat)[:,0],array(dat)[:,1],c=array(Ass))
	# plt.show()
# def demo_DDBSCAN():
	# # Create a DDBSCAN model with eps = 2 and min_pts = 5
	# data = loadDataSet('testSet.txt')
	# scan = ddbscan.DDBSCAN(1.2, 6)

	# # Add points to model
	# # data = [[1,  2], [2,  2], [1,  3], [2, 3], [3, 3], [8, 9],
			# # [7,  6], [9,  7], [6, 9], [6, 8], [5, 5], [7, 8]]

	# for point in data:
		# scan.add_point(point=point, count=1, desc="")

	# # Compute clusters
	# scan.compute()

	# print 'Clusters found and its members points index:'
	# cluster_number = 0
	# clustAssing = [-1]*len(data)
	# for cluster in scan.clusters:
		# print '=== Cluster %d ===' % cluster_number
		# templist = list(cluster)
		# print 'Cluster points index: %s' % templist
		# for n in templist:
			# clustAssing[n] = cluster_number
		# cluster_number += 1

	# print '\nCluster assigned to each point:'
	# for i in xrange(len(scan.points)):
		# print '=== Point: %s ===' % scan.points[i]
		# print 'Cluster: %2d' % scan.points_data[i].cluster,
		# # If a point cluster is -1, it's an anomaly
		# if scan.points_data[i].cluster == -1:
			# print '\t <== Anomaly found!'
		# else:
			# print
	
	# fig  = plt.figure()
	# ax = fig.add_subplot(121)
	# ax.scatter(array(data)[:,0],array(data)[:,1],c=array(clustAssing))
	# #ax1 = fig.add_subplot(122)
	# #ax1.scatter(array(dat)[:,0],array(dat)[:,1],c=array(Ass))
	# plt.show()
# if __name__ == '__main__':
	# demo_DDBSCAN()
	# demo_DBSCAN()
	
def reverse_sparse(termNumber,position):
	pos = array([0.0]*termNumber)
	pos[position] = 1.0
	return pos
	
def distEclud(A, B):
	vecA = set(A)
	vecB = set(B)
	return sqrt(len(vecA.union(vecB).difference(vecA.intersection(vecB)))) #la.norm(vecA-vecB)
	
def distCosin(A,B):
	vecA = set(A)
	vecB = set(B)
	innerProduct = len(vecA.intersection(vecB))
	#print "ineer product",innerProduct
	absA = sqrt(len(vecA))
	absB = sqrt(len(vecB))
	#print absA,absB
	return 1 - float((innerProduct))/(absA*absB)
	
def jaccard(a,b):
	aset = set(a)
	bset = set(b)
	return 1.0 - float(len(aset.intersection(bset)))/len(aset.union(bset))
	
def intersection(a,b):
	aset = set(a)
	bset = set(b)
	return 15-len(aset.intersection(bset))
	
def regionQuery(key,eps,dataset,distMean):
	self = dataset[key]
	resultSet = set([])
	for key in dataset:
		if distMean(self,dataset[key]) <= eps:
			resultSet.add(key)
	return resultSet
	
def sparse_dbscan(dataset,eps, minPts,distMean = jaccard):
	print "enter sparse_dbscan"
	clusterResult={}
	c = -1 
	visit_track = {}
	dataset.pop('len')
	for key in dataset.keys():
		status = visit_track.setdefault(key,{})
		status['isVisited'] = False
		status['class'] = 'None'
	#print visit_track
	for key in dataset.keys():
		if visit_track[key]['isVisited']:
			pass
		else:
			visit_track[key]['isVisited']=True
			NeighborPts = regionQuery(key,eps,dataset,distMean)
			if len(NeighborPts) < minPts:
				visit_track[key]['class'] = 'Noise'
			else:
				c = c + 1
				clusterResult.setdefault(c,[]).append(key)
				visit_track[key]['class'] = c
				exit = False
				NeighborPts_Update = NeighborPts.copy()
				while not exit:
					exit = True
					for p_ in NeighborPts:
						if not visit_track[p_]['isVisited']:
							visit_track[p_]['isVisited']=True
							NeighbotPts_prime = regionQuery(p_,eps,dataset,distMean)
							if len(NeighbotPts_prime) >= minPts:
								NeighborPts_Update = NeighborPts_Update.union(NeighbotPts_prime)
								exit = False
						if visit_track[p_]['class'] == 'None' or visit_track[p_]['class'] == 'Noise':
							clusterResult.setdefault(c,[]).append(p_)
							visit_track[p_]['class'] = c
					NeighborPts = NeighborPts_Update
	#print visit_track
	return 	clusterResult	
		
	
	
	