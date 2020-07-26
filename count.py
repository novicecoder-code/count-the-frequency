# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 19:40:00 2020

@author: HP
"""
import re
f = open("paragraph.txt", "r")
l=[]

for line in f:
    res = re.sub(r'[^\w\s]', '', line) 
    l.append(res.split())
d={}
for j in l:
    for i in j:
        d[i]=d.get(i,0)+1
print(d);