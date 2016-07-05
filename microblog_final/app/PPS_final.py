import nltk
import string
import re
import pickle
from sys import stdin
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords


def stopwordsRemoval(input_text):
    '''
    Handle a single line from the input file
    Transform uppercase string to lowercase
    Remove characters which are neither digits nor numbers
    Remove links start with 'http'
    Return a relatively neat list in which each element represents a raw token
    '''
    input_string = ''.join(str(element) for element in input_text if element not in string.punctuation)
    input_string = input_string.lower()
    input_words = wordpunct_tokenize(input_string)
    new_tokens = []
    for token in input_words:
        flag = 0
        token = re.sub(r'[^\w]', r'', token)
        if token[0:4] == 'http' or token[0:2] == 'rt':
            token = ''
        for stopword in stopwords.words('english'):
            if token == str(stopword):
                flag = 1
            if flag == 1:
                break
        if flag == 0:
            if token != '':
                new_tokens.append(token)
    return new_tokens

def wordSelection(fobj):
    '''
    Only keep nouns as tokens
    '''
    fobj = ' '.join(str(element) for element in fobj)
    tokens = nltk.word_tokenize(fobj)
    tagged = nltk.pos_tag(tokens)
    tokens = [line for line in tokens]
    tag = dict(tagged)
    tag_sel=[]
    addition = ['NNS', 'NN', 'NNP', 'JJ']
    for key in tag.keys():
        for feature in addition:
            if tag[key] == feature:
                tag_sel.append(key)
                break
    return tag_sel


def stemming(tokens):
    '''
    stemming
    '''
    stemmer1 = nltk.PorterStemmer()
    stemmer2 = nltk.LancasterStemmer()
    tokens_string = ''.join(str(element) for element in tokens if element not in string.punctuation)
    token_list = wordpunct_tokenize(tokens_string)
    stemmed_token = []
    for token in token_list:
        stemmer2.stem(token)
        stemmed_token.append(token)
    return stemmed_token

def Lemmatizing(token_list):
    '''
    Lemmatization
    '''
    lmtz = nltk.WordNetLemmatizer()
    lemmaed_tokens = []
    for token in token_list:
        lemma = lmtz.lemmatize(token)
        lemmaed_tokens.append(lemma.encode('utf-8'))
    return lemmaed_tokens

index = {}
def indexing2(lineList, day, rowNumber):
    '''Build index'''
    global index
    for word in lineList:
        indexForFile = {}
        if word in index:
            index[word][day].append(rowNumber)
        else:
            docIdList = []
            docIdList.append(rowNumber)
            indexForFile[day] = docIdList
            index[word] = indexForFile

def output(day):
    counter = 1
    inputFileName = 'input' + str(day) + '.txt'
    fr = open(inputFileName, 'r')
    outputFileName = 'output' + str(day) + '.txt'
    with open(outputFileName, 'w') as fw:
        for line in fr.readlines():
            ps_list1 = stopwordsRemoval(line)
            ps_list2 = wordSelection(ps_list1)
            ps_list3 = Lemmatizing(ps_list2)
            output = ' '.join(str(ele) for ele in ps_list3)
            fw.write(output)
            fw.write('\n')
            indexing2(ps_list3, day, counter)
            counter += 1
    fr.close
    fw.close


#output(1)
#print index
#with open ('index.pickle', 'wb') as handle:
    #pickle.dump(index, handle)

