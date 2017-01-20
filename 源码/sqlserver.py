# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:40:55 2016

@author: xc
"""

import pymssql
import random
class connectDB():
    def __init__(self):
        self.conn = pymssql.connect(host="localhost",user="sa",password="12345", database="apriori")
        self.cur = self.conn.cursor()
        
    def query(self,sql):
        self.cur.execute(sql)
        rows=self.cur.fetchall()
        self.conn.close()
        return rows

db=connectDB()
rows=db.query("select * from test")
print(rows)
#cur.execute("select * from tab01")
#rows=cur.fetchall()     #读取数据库  取出所有记录
#conn.close()
#count = 0
#for item in rows:
#    count+=1
#    
#print(count)

#for i in range(0,2000000):
#    A=random.choice('A ')
#    B=random.choice('B ')
#    C=random.choice('C ')
#    D=random.choice('E ')
#    E=random.choice('E ')
#    F=random.choice('F ')
#    G=random.choice('G ')
#    H=random.choice('H ')
#    I=random.choice('I ')
#    J=random.choice('J ')
#    sql="insert into tab100 values("+"'"+A+"','"+B+"','"+C+"','"+D+"','"+E+"','"+F+"','"+G+"','"+H+"','"+I+"','"+J+"')"
#    print(sql)
#    cur.execute(sql)
#    conn.commit()

#conn.close()


        