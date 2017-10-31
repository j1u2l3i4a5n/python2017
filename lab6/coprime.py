# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:48:56 2017

@author: rjlin
"""

def devisor(num):
    devise = []
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            devise.append(i)
    devise.append(num)
    return set(devise)

def coprimeTest(*inputNum):
    setList = []
    for i in inputNum:
        setList.append(devisor(i))
    s = setList[0]
    for i in setList:
        s &= i
    if s == set():
        return True
    else:
        return False

