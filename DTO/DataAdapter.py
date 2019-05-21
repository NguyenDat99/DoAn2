# coding=utf-8
import pandas as pd
import numpy as np
csv1=pd.read_csv('../DTO/dataset/CSV/data1.csv',encoding='utf-8')
csv2=pd.read_csv('../DTO/dataset/CSV/data2.csv',encoding='utf-8')
from multiprocessing.dummy import Pool as ThreadPool


def getFeature1(name):
    return (csv1[name].values).tolist()

def getFeature2(name):
    return (csv2[name].values).tolist()


def multiprocessing(k):
    t=['text','label']
    pool = ThreadPool(2)
    if k==1:
        data=pool.map(getFeature1,t)
    elif k==2:
        data=pool.map(getFeature2,t)
    return data

def loaiTru(s):
    for i in s:
        if i =='.' or i=='?' or i==',' or i=='0' or i==' ' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7'or i=='8' or i=='9' or i==')'or i=='('or i=='"'or i=='='or i=='>'or i=='<'or i=='&'or i=='^'or i=='*'or i=='%'or i=='#'or i=='$'or i==''or i=='@'or i==':' or i==';':
            return 0
    return 1

def locKiTuDacBiet(s):
    s1=""
    if s!='href' and s!='class' and s!='hashtag-link' and s!= '\n':
        for i in range(len(s)):
            if s[i]!='!' and s[i] !='/'and s[i] !='.'and s[i] !="'":
                    s1+=s[i]
    return s1

def lamSachChuoi(text):
    s=""
    k=text.split(" ")
    for j in k:
        if loaiTru(j)==1:
            s+=locKiTuDacBiet(j)+" "
    return s

def ExCSV():
    dt=[]
    for i in range(1,1000): #35473
        try:
            file=open('../DTO/dataset/pos/%s.txt'%i,"r")
            dt.append([lamSachChuoi(file.read()),1])
            file.close()
        except:
            a=2
    for i in range(1,1000):#29246
        try:
            file=open('../DTO/dataset/neg/%s.txt'%i,"r")
            dt.append([lamSachChuoi(file.read()),0])
            file.close()
        except:
            a=2
    dt=np.array(dt)
    df = pd.DataFrame({'text':dt[:,0],'label':dt[:,1]})
    df.to_csv('../DTO/dataset/CSV/data2.csv',encoding='utf-8',index=False)

#ExCSV()
class dataset:
    def __init__(seft,k):
        data=multiprocessing(k)
        seft.text=data[0]
        seft.label=data[1]
