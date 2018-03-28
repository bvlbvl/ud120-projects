#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus, color="b" )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

#import operator
#data_dict_sorted = sorted (data_dict.items(), key = operator.itemgetter(1))

import operator
index_max, value_max = max(enumerate(data[0]), key=operator.itemgetter(1))


bla = data_dict["TOTAL"]
data_dict_wo_TOTAL = data_dict
data_dict_wo_TOTAL.pop("TOTAL", 0)

data_wo_TOTAL = featureFormat(data_dict_wo_TOTAL, features)
### your code below
for point in data_wo_TOTAL:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus, color="b" )

matplotlib.pyplot.xlabel("salary without outliers")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

#%%
for key, value in data_dict_wo_TOTAL.iteritems():
    bonus = value["bonus"]
    if ((bonus >= 5000000) and (bonus != "NaN")):
        print key