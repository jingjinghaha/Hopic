import pickle

def grabIndex(filename):
	fr = open(filename)	
	return pickle.load(fr)

def storeindex(index,filename):
	fw = open(filename,'w')
	pickle.dump(index,fw)
	fw.close()

def prediction(cf1,cf2,cf3,cf4,cf5,cf6,cf7):
	import numpy as np
	from sklearn import linear_model
	data_x_train = [[1], [2], [3], [4], [5], [6], [7]]
	data_y_train = [[1.2], [2.1], [3.4], [4.2], [5.6], [6.1], [7.8]]
	data_x_test = [8]
	data_y_test = [8.4]

	# regr = linear_model.LinearRegression()
	# regr.fit(data_x_train, data_y_train)
	# # print(regr.coef_)
	# # print(regr.intercept_)
	# # print(regr.predict(data_x_test))

	# clf = linear_model.Ridge(alpha = .5)
	# clf.fit(data_x_train, data_y_train) 
	# # print(clf.coef_)
	# # print(clf.intercept_)
	# # print(clf.predict(data_x_test))

	# clf = linear_model.Lasso(alpha = 0.1)
	# clf.fit(data_x_train, data_y_train)
	# # print(clf.predict(data_x_test))
	# # return clf.predict(data_x_test)

	# # clf = linear_model.BayesianRidge()
	# # clf.fit(data_x_train, data_y_train)
	# # print(clf.predict(data_x_test))

	data_y_train[0][0] = cf1
	data_y_train[1][0] = cf2
	data_y_train[2][0] = cf3
	data_y_train[3][0] = cf4
	data_y_train[4][0] = cf5
	data_y_train[5][0] = cf6
	data_y_train[6][0] = cf7

	clf = linear_model.Lasso(alpha = 0.9)
	clf.fit(data_x_train, data_y_train)
	# print(clf.predict(data_x_test))
	return clf.predict(data_x_test)

# a =  prediction(1,2,3,4,5,6,7) 
# print a[0]

DF = grabIndex('DF.pickle')
for key in DF:
	value = prediction(DF[key][0],DF[key][1],DF[key][2],DF[key][3],DF[key][4],DF[key][5],DF[key][6])
	temp = value[0]
	DF[key].append(temp) 
storeindex(DF,'DF_Lasso_0.9.pickle')
