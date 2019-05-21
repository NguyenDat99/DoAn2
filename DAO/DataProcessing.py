# coding=utf-8
import sys
sys.path.append('../DTO/')
import pandas as pd
import DataAdapter as da
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from pyvi import ViTokenizer, ViPosTagger
data=da.dataset(2)

def demTu(dt):
    k =dt.split(" ")
    dem=0
    for i in k:
        if i !=" ":
            dem+=1
    return dem

def bag_of_words(dt):
    tuDien=[]
    s=[]
    s1=[]
    # cat chuoi tung cau noi lai
    for i in range(len(dt)):
        k=dt[i].split(" ")
        for j in k:
            if j!=' ':
                s.append(j)
    #loc trung
    for i in range(len(s)):
        if s[i] not in s1:
            s1.append(s[i])
    #bo tu dien
    for i in range(len(dt)):
        array=[]
        k=dt[i].split(" ")
        for j in s1:
            dem=0
            if j not in k:
                array.append([j,0])
            else:
                for h in k:
                    if j ==h:
                        dem+=1
                array.append([j,dem])
        tuDien.append(np.array(array))
    return tuDien

def tinhTF(dt,tuDien):
    array=[]
    tongTu=demTu(dt)
    for tu, chiSo in tuDien:
        if tu!=' ':
            array.append([tu,float(chiSo)/tongTu])
    return np.array(array)

def tinhIDF(dt,tuDien):
    array=[]
    tongCau=len(dt)
    dem=0
    for tu, chiSo in tuDien[0]:
        for cau in dt:
            if tu in cau.split():
                dem+=1
        if(dem>0):
            array.append([tu,float(tongCau)/dem])
        dem=0
    return np.array(array)

def tinhTF_IDF(tuDienTF,tuDienIDF):
    array=[]
    for tu_tf, chiSo_tf in tuDienTF:
        for tu_idf, chiSo_idf  in tuDienIDF:
            if tu_tf==tu_idf:
                array.append([tu_tf,float(chiSo_tf)*float(chiSo_idf)])
    return np.array(array)

def locTF_IDF(tuDienTF_IDF):
    array=[]
    for tu, chiSo in tuDienTF_IDF:
        if(chiSo>0.2):
            array.append([tu,chiSo])
    return np.array(tuDienTF_IDF)

def tuDien():
    dt=data.text
    tuDien=bag_of_words(dt)
    tuDienTF=tuDien
    tuDienIDF=[]
    tuDienTF_IDF=tuDien
    #tinhTF
    tuDienTF=tuDien
    for i in range(len(dt)):
        tuDienTF[i]=tinhTF(dt[i],tuDien[i])
    #tinhIDF
    tuDienIDF=tinhIDF(dt,tuDien)
    #tinhTF_IDF
    for i in range(len(tuDienTF)):
        tuDienTF_IDF[i]=tinhTF_IDF(tuDienTF[i],tuDienIDF)
    for i in range(len(tuDienTF_IDF)):
        tuDienTF_IDF[i]=locTF_IDF(tuDienTF_IDF[i])

    print(tuDienTF_IDF[0])


    print(tinhTF_IDF(tuDienTF[0],tuDienIDF))
tuDien()
