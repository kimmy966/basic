#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 17:16:54 2018

@author: kimmy
"""

import numpy as np

def metrix_point_division(a,b,shape):
    c = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            if b[i][j] == 0:
                c[i][j] = np.nan
            else:
                c[i][j] = a[i][j] / b[i][j]
    return c
