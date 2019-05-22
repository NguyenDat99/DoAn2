# coding=utf-8
import sys
sys.path.append('../DAO/')
import DataProcessing as dp
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test=train_test_split(
dp.dataSet(),
dp.label(),
test_size=0.2,random_state=1)



def Knn():
    clf=KNeighborsClassifier(n_neighbors=3).fit(x_train,y_train)
    precision= precision_score(y_test,clf.predict(x_test), average='weighted')
    recall= recall_score(y_test,clf.predict(x_test), average='weighted')
    F=(2*precision*recall)/(precision+recall)
    return F

print(Knn())
