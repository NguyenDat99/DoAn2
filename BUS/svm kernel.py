import sys
sys.path.append('../DAO/')
import DataProcessing as dp
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def Svmker():
    x_train, x_test, y_train, y_test=train_test_split(
    dp.dataSet(2),
    dp.label(2),
    test_size=0.1,random_state=1)
    grid = [{'kernel': ['rbf'], 'gamma': [1e-2, 1e-4],
                    'C': [1, 10, 100]}]
    grid = GridSearchCV(SVC(), grid, cv=5)
    grid.fit(x_train, y_train)
    print("The best parameters are %s with a score of %0.2f"% (grid.best_params_, grid.best_score_))

 










