# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:47:14 2017

@author: rjlin
"""

inputFile=open("filename.txt",'r')
data=inputFile.read()
dataList=data.split(' ')
for i in range(len(dataList)):
    dataList[i]=int(dataList[i])

