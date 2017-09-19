# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:47:14 2017

@author: rjlin
"""

inputFile=open("filename.txt",'r')
data=inputFile.read()
inputFile.close()
dataList=data.split(' ')
dataStr=""
temp=[]

for i in range(len(dataList)):
    dataList[i]=int(dataList[i])
    
for i in range(len(dataList)):
    dataList[i]=dataList[i]**2

for i in  [17, 23, 46, 78, 91]:
    dataList.append(i)

for i in range(len(dataList)): 
    temp.append(dataList[len(dataList)-i-1])
dataList=temp
    
for i in dataList:
    dataStr+=str(i)+" "

outputFile=open("output.txt","w")
outputFile.write(dataStr)
outputFile.close()
