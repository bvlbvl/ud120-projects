# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:25:04 2018

@author: MV
"""

import math
import numpy

examples = [1, 2]
sumExamples = numpy.sum(examples)
entropy = 0
for i in examples:
    p = float(i)  / sumExamples
    print i, p, sumExamples
    entropy = entropy - p * math.log(p, 2)

print entropy    