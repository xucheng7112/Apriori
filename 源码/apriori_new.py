 # -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:35:48 2016

@author: xc
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 13:13:08 2016

@author: xc
"""

import copy
import pymssql
import time
import csv 

def init_data():
    try:
        conn = pymssql.connect(host="localhost",user="sa",password="12345", database="apriori")
    except pymssql.OperationalError:
        print( "error: Could not Connection SQL Server!please check your dblink configure!")
    else:
        cur = conn.cursor()
        
    cur.execute("select * from tab20")
    rows=cur.fetchall()     #读取数据库  取出所有记录
    conn.close()
        
    T=[]
    count=0
    for item in rows:
        T.append([])
        for i in item:
            if i != ' ':
                T[count].append(i)
        count+=1
#        
#    for item in T:
#        print(item)
        
    return T
    
    
#初始化所有一项集
def init_pass(T):
    C = {}  #C为字典
    for t in T: 
        for i in t:

            if i in C.keys():
                C[i] += 1
            else:
                C[i] = 1
    return C

def generate(F):
    C = []
    k = len(F[0]) + 1
    for f1 in F:
        for f2 in F:
            if f1[k-2] < f2[k-2]:
                c = copy.copy(f1)
                c.append(f2[k-2])
                flag = True
                for i in range(0,k-1):
                    s = copy.copy(c)
                    s.pop(i)
                    if s not in F:
                        flag = False
                        break
                if flag and c not in C:
                    C.append(c)

    return C

def compareList(A,B):
    for a in A:
        if a not in B:
            return False
    return True
    
def apriori(T,minSupport):
    D=[]
    C=init_pass(T)
    keys=C.keys();#.keys()方法，求出字典中的索引

    D.append(sorted(keys))#加入D集中
    F=[[]]

    for f in D[0]:
        if C[f]>=minSupport:
            F[0].append([f])
    k=1
#    print(F)

#    while F[k-1]!=[]:
#        D.append(generate(F[k-1]))
#        F.append([])
#        for c in D[k]:
#            count = 0;
#            for t in T:
#                if compareList(c,t):
#                    count += 1
#            if count>= minSupport:
#                F[k].append(c)
#        k += 1
    while F[k-1]!=[]:
        D.append(generate(F[k-1]))
        F.append([])
        count={}
        for t in T:
            i=0
            for c in D[k]:
                if compareList(c,t):
                    if i in count.keys():
                        count[i] += 1
                    else:
                        count[i] = 1
                i+=1
#        print(count)
        for i in count:
            if count[i]>=minSupport:
                F[k].append(D[k][i])
#        print(F)
        
        k+=1

    U = []
    for f in F:
        for x in f:
            U.append(x)
    return U

if __name__ == "__main__":
    start=time.clock()
    T=init_data()
    Z= apriori(T,100000)
    
    try:
        datacsv=open(r'C:\Users\xc\Desktop\test.csv',"w",newline="") 
        csvwriter = csv.writer(datacsv)
        for item in Z:
            print(item)
            csvwriter.writerow(item)
        datacsv.close()
    except:
        pass
    print(time.clock()-start)
