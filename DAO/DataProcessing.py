# coding=utf-8
import sys
sys.path.append('../DTO/')
import pandas as pd
import DataAdapter as da
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler



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
        if(float(chiSo)>0.01):
            array.append([tu,chiSo])
    return np.array(array)

def xuLyTF_IDF(data):
    dt=data.text
    tuDien=bag_of_words(dt)
    tuDienTF=tuDien
    tuDienIDF=[]
    tuDienTF_IDF=[]
    #tinhTF
    tuDienTF=tuDien
    for i in range(len(dt)):
        tuDienTF[i]=tinhTF(dt[i],tuDien[i])
    #tinhIDF
    tuDienIDF=tinhIDF(dt,tuDien)
    #tinhTF_IDF
    for i in range(len(tuDienTF)):
        tuDienTF_IDF.append(tinhTF_IDF(tuDienTF[i],tuDienIDF))
    for i in range(len(tuDienTF_IDF)):
         tuDienTF_IDF[i]=(locTF_IDF(tuDienTF_IDF[i]))
    return np.array(tuDienTF_IDF)


def tienXuLy(data):
    s=xuLyTF_IDF(data)
    array1=[]
    array2=[]
    for cau in s:
        for tu, chiSo in cau:
            array1.append(tu)
    for i in array1:
        if i not in array2:
            array2.append(i)
    return np.array(array2)



def chuyenSangSo(dt,tuDien):
    k=dt.split()
    a=[]
    for i in tuDien:
        a.append(0)
    a=np.array(a)
    for i in k:
        for j in range(len(tuDien)):
            if  i==tuDien[j]:
                a[j]=1
    return a

def dataSet(k):
    data=[]
    if k==1:
        data=da.dataset(1)
    elif k==2:
        data=da.dataset(2)
    dt=data.text
    dataset=[]
    tuDien=tienXuLy(data)
    for i in range(len(dt)):
        dataset.append(chuyenSangSo(dt[i],tuDien))
    #rut  chieu du lieu
    dataset=np.array(dataset)
    sc = StandardScaler()
    X = sc.fit_transform(dataset)
    pca = PCA(n_components=3)
    X_pca = pca.fit_transform(X)
    print("\n\n\n\t\t\t Xu ly du lieu thanh cong! ")
    return X_pca

def label(k):
    data=[]
    if k==1:
        data=da.dataset(1)
    elif k==2:
        data=da.dataset(2)
    return data.label
