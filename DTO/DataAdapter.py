# coding=utf-8
import pandas as pd
import numpy as np
csv1=pd.read_csv('../DTO/dataset/CSV/data1.csv',encoding='utf-8')
csv2=pd.read_csv('../DTO/dataset/CSV/data2.csv',encoding='utf-8')
from multiprocessing.dummy import Pool as ThreadPool
from pyvi import ViTokenizer, ViPosTagger

#67190 Câu

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
        if i =='.' or i=='?' or i==',' or i=='0' or i==' ' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7'or i=='8' or i=='9' or i==')'or i=='('or i=='"'or i=='='or i=='>'or i=='<'or i=='&'or i=='^'or i=='*'or i=='%'or i=='#'or i=='$'or i==''or i=='@'or i==':' or i==';'or i=='-'or i=='+'or i=='^'or i=='&'or i=='|'or i=='{'or i=='}':
            return 0
    return 1

def locKiTuDacBiet(s):
    s1=""
    s2=""
    if s!='href' and s!='class' and s!='hashtag-link' and s!= '\n' and s!='thì' and s!='là'and s!='ở'and s!='đi'and s!='tao'and s!='mày'and s!='cây'and s!='đến'and s!='vừng'and s!='bán'and s!='đồ ăn'and s!='Đồ ăn'and s!='cơm_chiên'and s!='vô'and s!='cách'and s!='đây'and s!='Vị_trí'and s!='bánh_bao'and s!='Kem'and s!='từ'and s!='ngoài'and s!='vô'and s!='của'and s!='xe'and s!='thứ'and s!='hôm'and s!='đó'and s!='kho'and s!='quẹt'and s!='buổi_sáng'and s!='Xe_đẩy'and s!='decor'and s!='i'and s!='o'and s!='đươ'and s!='c'and s!='n'and s!='cu'and s!='_' and s!='service'and s!='Menu' and s!='bad'and s!='ㅠ'and s!='bill'and s!='Matcha'and s!='green'and s!='almond'and s!='chocolate'and s!='PERFECT'and s!='kpop'and s!='SG'and s!='upstair'and s!='driving'and s!='in'and s!='to'and s!='check'and s!='say'and s!='ran':
        for i in range(len(s)):
            if s[i]!='!' and s[i] !='/'and s[i] !='.'and s[i] !="'" :#and s[i]!='['and s[i]!=']'and s[i]!='|'and s[i]!='{'and s[i]!='}'and s[i]!=';'and s[i]!=','
                    s1+=s[i]
    s1.rstrip("\n")
    s3=ViPosTagger.postagging(ViTokenizer.tokenize(u"%s"%s1))
    for i in range(len(s3[0])):
        if s3[1][i]!='N'and s3[1][i]!='Np'and s3[1][i]!='P' and s3[1][i]!='E'and s3[1][i]!='T'and s3[1][i]!='L'and s3[1][i]!='M':
            s2+=s3[0][i]+" "
    return s2

def lamSachChuoi(text):
    s=""
    k=text.split(" ")
    for j in k:
        if loaiTru(j)==1:
            s+=locKiTuDacBiet(j)+" "
    return s


def ExCSV():
    dt=[]
    for i in range(1,25): #35473
        try:
            file=open('../DTO/dataset/pos/%s.txt'%i,"r")
            dt.append([lamSachChuoi(lamSachChuoi(file.read())),1])
            file.close()
        except:
            a=2
    for i in range(1,25):#29246
        try:
            file=open('../DTO/dataset/neg/%s.txt'%i,"r")
            dt.append([lamSachChuoi(lamSachChuoi(file.read())),0])
            file.close()
        except:
            a=2
    dt=np.array(dt)
    df = pd.DataFrame({'text':dt[:,0],'label':dt[:,1]})
    df.to_csv('../DTO/dataset/CSV/data2.csv',encoding='utf-8',index=False)
    #lam sach lai

ExCSV()
class dataset:
    def __init__(seft,k):
        data=multiprocessing(k)
        if k==1:
            dt1=[]
            dt2=[]
            for i in range(len(data[0])):
                if lamSachChuoi(data[0][i])!=None:
                    dt1.append(lamSachChuoi(data[0][i]))
                    dt2.append(data[1][i])
            seft.text=dt1
            seft.label=dt2
        elif k==2:
            seft.text=data[0]
            seft.label=data[1]
