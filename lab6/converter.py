# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 21:22:51 2017

@author: rjlin
"""
codeDict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}

def converter(inputNum, carry):
    #inpuType inputNum = int, carry = int
    intPart = int(inputNum)
    left = intPart % carry
    devide = int(intPart / carry)
    if devide != 0:
        return converter(devide, carry) + codeDict[left]
    else:
        return codeDict[left]
    
def converterFloat(inputNum, carry):
    floatPart = inputNum - int(inputNum)
    left = int(floatPart * carry)
    devide = floatPart * carry - int(floatPart * carry)
    if devide != 0:
        return converterFloat(devide, carry) + codeDict[left]
    else:
        return codeDict[left]
    
def combine(inputNum, carry):
    
    if int(inputNum) == inputNum:
        if inputNum > 0:
            return converter(inputNum, carry)
        else:
            return '-' + converter(abs(inputNum), carry)
    else:
        if inputNum > 0:
            return converter(inputNum, carry) + '.' +converterFloat(inputNum, carry)
        else:
            return '-' + converter(abs(inputNum), carry) + '.' +converterFloat(abs(inputNum), carry)
    
