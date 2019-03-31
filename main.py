# coding=utf-8
import pandas as pd
from pyvi import ViTokenizer, ViPosTagger

data=[]
DauVao=pd.read_csv('./data/training/TrainingData.csv',encoding='utf-8')
x_training=(DauVao['DauVao'].values).tolist()
y_Training=(DauVao['Nhan'].values).tolist()

for i in range(len(x_training)):
    k =ViPosTagger.postagging(ViTokenizer.tokenize(u"%s" %x_training[i]))
    data.append([k[0],k[1]])

print(data[12])

#from sklearn.feature_extraction import DictVectorizer
#X=[{'a':'N'},{'b':'3'},{'c':'3'},{'d':'3'}]
#vec = DictVectorizer()
#print(vec.fit_transform(data).toarray())
