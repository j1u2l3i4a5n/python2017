# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:43:19 2017

@author: rjlin
"""


def readFile(filename):
    file = open(filename, 'r')
    data = file.read()
    file.close
    return data

def stringToMatrix(inputStr):
    #input a string with csv format
    matrix = inputStr.split('\n')
    matrix.pop()
    for index in range(len(matrix)):
        matrix[index] = matrix[index].split(',')
    return matrix

def matrixRotate(matrix):
    rowSize = len(matrix)
    columnSize = len(matrix[0])
    output=[]
    for i in range(columnSize):
        temp = []
        for j in range(rowSize):
            temp.append([0])
        output.append(temp)
    for i in range(columnSize):
        for j in range(rowSize):
            temp = matrix[j][i]
            output[i][rowSize - j - 1] = temp
    return output

def matrixRotateCheck(matrix1, matrix2):
    #check matrix2 could be made by rotating matrix1
    #input type matrix1:list matrix2:list
    #output type Boolean
    output = False
    for i in range(4):
        if matrix1 == matrix2:
            output = True
        matrix1 = matrixRotate(matrix1)
    
    return output

def pipeline(file1,file2):
    data1 = readFile(file1)
    data2 = readFile(file2)
    matrix1 = stringToMatrix(data1)
    matrix2 = stringToMatrix(data2)
    print(matrixRotateCheck(matrix1, matrix2))

if __name__ == '__main__':
    pipeline('table1.csv','table2.csv')
    
        
        
        