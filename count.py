# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 19:40:00 2020

@author: HP
"""

s=input("enter the string\n")
l=s.split();
d={}
for i in l:
     d[i]=d.get(i,0)+1
print(d);