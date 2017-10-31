# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:21:36 2017

@author: rjlin
"""

import coprime

def coprimeGen(start, num):
    output  = []
    check = start + 1
    while len(output) < num:
        if coprime.coprimeTest(start, check):
            output.append(check)
        check += 1
    return output