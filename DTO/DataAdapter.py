# coding=utf-8
import pandas as pd
csv=pd.read_csv('../DTO/dataset/CSV/data.csv',encoding='utf-8')
from multiprocessing.dummy import Pool as ThreadPool

def getFeature(file,name):
    return (file[name].values).tolist()
# def getFeature(file):
#     return (file.values).tolist()
def getFeature(name):
    return (csv[name].values).tolist()


def multiprocessing():
    t=['text','label']
    pool = ThreadPool(2)
    data=pool.map(getFeature,t)
    return data

def ExCSV():
    array=[]
    # for i in range(1,300): #35473
    #     try:
    #         PosFile1 = pd.read_csv('../DTO/dataset/data_train/pos/%s.txt'%i, sep=" ", header=None)
    #         print(PosFile1[0])
    #         array.append([getFeature(PosFile1),1])
    #     except:
    #         a=2
    # for i in range(1,29244):
    #     try:
    #         PosFile1 = pd.read_csv('../DTO/dataset/data_train/neg/%s.txt'%i, sep=" ", header=None)
    #         if PosFile1!=None:
    #             array.append(getFeature([getFeature(PosFile1),0])
    #     except:
    #         a=2
    # for i in range(1,35467):
    #     try:
    #         PosFile1 = pd.read_csv('../DTO/dataset/data_test/pos/%s.txt'%i, sep=" ", header=None)
    #         if PosFile1!=None:
    #             array.append(getFeature([getFeature(PosFile1),1]))
    #     except:
    #         a=2
    # for i in range(1,29246):
    #     try:
    #         PosFile1 = pd.read_csv('../DTO/dataset/data_test/neg/%s.txt'%i, sep=" ", header=None)
    #         if PosFile1!=None:
    #             array.append([getFeature(PosFile1),0])
    #     except:
    #         a=2
    return  array
class dataset:
    def __init__(seft):
        data=multiprocessing()
        seft.text=data[0]
        seft.label=data[1]
