from flask import render_template
from flask import request
from app import app
from flask import render_template, flash, redirect, send_from_directory
import spellChecking
import fullTextSearch
import nltk
import pickle
import random
import PPS_final

tweetsList = {}
indexList = {}
fileCluster = {}
for fileNum in range(1, 8):
    fr1 = open('inputList' + str(fileNum) + '.pickle')
    tweetsList[fileNum] = pickle.load(fr1)
    fr2 = open('index' + str(fileNum) + '.pickle')
    indexList[fileNum] = pickle.load(fr2)
    fr1.close()
    fr2.close()
#fr3 = open('clusters.pickle')
#clustersDict = pickle.load(fr3)
#fr3.close()
fr4 = open('prediction.pickle')
forecastDict = pickle.load(fr4)
fr4.close()
fr5 = open('IDFnew.pickle')
idfDict = pickle.load(fr5)
fr5.close()
for fileNum in range(1, 15):
    fr6 = open('filecluster' + str(fileNum) + '.pickle')
    fileCluster[fileNum] = pickle.load(fr6)
    fr6.close()

@app.route('/', methods = ['GET'])
def index():
    return render_template('search.html')

@app.route('/results', methods = ['GET'])
def results():
    query = request.args.get('query')
    query = query.lower()
    queryList = query.split()
    query = PPS_final.Lemmatizing(query)
    queryString = ''
    for word in queryList:
        word = spellChecking.correct(word)
        queryString += word + ' '
    query = queryString
    queryString2 = queryString.split()
    results = []
    for id in range(1, 8):
        scoredIndex = fullTextSearch.getIdfScoredIndex(id, queryString2, indexList[id], idfDict)
        for lineNum in scoredIndex:
            results.append(tweetsList[id][lineNum-1].decode('utf-8'))
    return render_template('results.html', query = query, results = results)


@app.route('/clustering')
def clustering():
    positionOfCenter = [{'x': 360, 'y': 225}, {'x': 720, 'y': 225}, {'x': 1080, 'y': 225}, {'x': 1440, 'y': 225},
    {'x': 300, 'y': 450}, {'x': 600, 'y': 450}, {'x': 900, 'y': 450}, {'x': 1200, 'y': 450}, {'x': 1500, 'y': 450},
    {'x': 300, 'y': 675}, {'x': 600, 'y': 675}, {'x': 900, 'y': 675}, {'x': 1200, 'y': 675}, {'x': 1500, 'y': 675}]
    position = {}
    for cluster in range(1, 15):
        length = len(fileCluster[cluster])
        position[cluster] = []
        for ele in range(0, length):
            pointPosition = {}
            pointPosition['x'] = 90 * random.uniform(-1, 1) * (random.uniform(-1, 1) + 1) + positionOfCenter[cluster-1]['x']
            pointPosition['y'] = 90 * random.uniform(-1, 1) * (random.uniform(-1, 1) + 1) + positionOfCenter[cluster-1]['y']
            pointPosition['id'] = fileCluster[cluster][ele].decode('utf-8')
            position[cluster].append(pointPosition)
    position1 = position[1]
    position2 = position[2]
    position3 = position[3]
    position4 = position[4]
    position5 = position[5]
    position6 = position[6]
    position7 = position[7]
    position8 = position[8]
    position9 = position[9]
    position10 = position[10]
    position11 = position[11]
    position12 = position[12]
    position13 = position[13]
    position14 = position[14]
    return render_template('clustering.html', position1 = position1, position2 = position2, position3 = position3,
    position4 = position4, position5 = position5, position6 = position6, position7 = position7, position8 = position8,
    position9 = position9, position10 = position10, position11 = position11, position12 = position12, position13 = position13,
    position14 = position14)

@app.route('/forecast', methods=['GET'])
def forecast():
    query = request.args.get('query')
    query = query.lower()
    queryList = query.split()
    queryString = ''
    for word in queryList:
        word = spellChecking.correct(word)
        queryString += word
    query = queryString
    if query in forecastDict:
        d1 = forecastDict[query][0]
        d2 = forecastDict[query][1]
        d3 = forecastDict[query][2]
        d4 = forecastDict[query][3]
        d5 = forecastDict[query][4]
        d6 = forecastDict[query][5]
        d7 = forecastDict[query][6]
        d8 = forecastDict[query][8]
    else:
        d1 = 0
        d2 = 0
        d3 = 0
        d4 = 0
        d5 = 0
        d6 = 0
        d7 = 0
        d8 = 0
    return render_template('forecast.html', d1 = d1, d2 = d2, d3 = d3, d4 = d4, d5 = d5, d6 = d6, d7= d7, d8 = d8)


