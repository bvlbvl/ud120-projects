# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 23:33:48 2018

@author: MV
"""

""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    min_val = min(arr)
    max_val = max(arr)
    ret = []
    for x in arr:
        ret.append((x - min_val + 0.0)/(max_val - min_val + 0.0))

    return ret

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)