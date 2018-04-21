# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 22:40:32 2018

@author: MV
"""
import nltk
nltk.download("stopwords")

from nltk.corpus import stopwords
sw = stopwords.words("english")
print len(sw)