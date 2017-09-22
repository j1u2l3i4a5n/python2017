# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:47:14 2017

@author: rjlin
"""

inputFile=open("filename.txt",'r')
data=inputFile.read()
inputFile.close()

output=' '.join(map(str,(map(lambda x:x**2,map(int,data.split(' ')))+[17, 23, 46, 78, 91])[::-1]))

outputFile=open("output.txt","w")
outputFile.write(output)
outputFile.close()
