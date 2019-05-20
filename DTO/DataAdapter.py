# coding=utf-8
import pandas as pd

csv1=pd.read_csv('../DTO/dataset/CSV/data1.csv',encoding='utf-8')
csv2=pd.read_csv('../DTO/dataset/CSV/data2.csv',encoding='utf-8')

def getFeature(file,name):
    return (file[name].values).tolist()
def getFeature(file):
    return (file.values).tolist()

def ExCSV():
    array=[]
    for i in range(1,35473):
        try:
            PosFile1 = pd.read_csv('../DTO/dataset/data_train/pos/%s.txt'%i, sep=" ", header=None)
            if PosFile1!=None:
                array.append([getFeature(PosFile1),1])
        except:
            a=2
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
    return array
class dataset:
    def __init__(seft,text,label):
        seft.text=text
        seft.label=label

print(ExCSV())
