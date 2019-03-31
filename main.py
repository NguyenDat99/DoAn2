# coding=utf-8
import csv
import numpy as np
import pandas as pd
from pyvi import ViTokenizer, ViPosTagger

data=[]
DauVao=pd.read_csv('./data/training/TrainingData.csv',encoding='utf-8')
data.append([(DauVao['DauVao'].values).tolist(),(DauVao['Nhan'].values).tolist()])
data=np.array(data)

#print(ViPosTagger.postagging(ViTokenizer.tokenize(u"%s" %data[:,0])))
#X=ViPosTagger.postagging(ViTokenizer.tokenize(u"tôi đang sống chốn nào thế " ))
from sklearn.feature_extraction import DictVectorizer
X=[{'a':'1'},{'b':'2'},{'c':'3'},{'d':'1'},{'e':'3'}]
vec = DictVectorizer()
print(vec.fit_transform(X).toarray())
