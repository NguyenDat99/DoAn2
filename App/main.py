# coding=utf-8
import sys
sys.path.append('../BUS/')
import knn

def KNN(k):
    a=knn.Knn(k) *100
    s="\t\t\tketqua: "+str(a)+" %"
    print(s)
