# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:42:02 2018

@author: lenovo
"""

import numpy as np

x = np.array([3,5,7,1,9,8,6,6])
y = np.array([2,1,5,10,100,6])

def findIdx_fuc(x,y):
    
    flag = np.in1d(x,y,invert = True)
    
    result = np.searchsorted(y, x, sorter = np.argsort(y))
    
    result[flag] = 0
    
    return result

#tests

c = findIdx_fuc(x,y)


def lag(X,lenth):
    res = np.full_like(np.array(X),np.nan)
    if lenth >= 0:
        res[lenth:,:] = np.array(X)[:-lenth,:]
    else:
        res[:(len(X[0,:]))+lenth,:] = X[-lenth:,:]
    return res