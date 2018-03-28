#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#%%
enron_data_len = len(enron_data)
print "data length =", enron_data_len

enron_data_num_val = len(enron_data.values()[0])
print "num of items per value =", enron_data_num_val

from collections import Counter

c = Counter(enron_data)
#print c

num_poi = 0 

for value in enron_data.itervalues():
#    print value
    if value["poi"]:
        num_poi = num_poi + 1
print "num pois= ", num_poi

#%%
print enron_data["PRENTICE JAMES"]

print enron_data["COLWELL WESLEY"]




print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
#%%

num_qntsalary = 0
num_email = 0 

for value in enron_data.itervalues():
#    print value
    if value["salary"] != "NaN":
        num_qntsalary += 1
    if value["email_address"] != "NaN":
        num_email += 1
print "num_qntsalary = ", num_qntsalary
print "num_email = ", num_email