#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree

t0 = time()
clf1 = tree.DecisionTreeClassifier(min_samples_split = 40)
clf1.fit(features_train, labels_train)
print "Fit time: ", time() - t0

t1= time()
pred = clf1.predict(features_test)
print "Predict time: ", time() - t1

from sklearn.metrics import accuracy_score
print "accuracy:", accuracy_score(labels_test, pred)
print "num of features", len(features_train[0])
#%%perc 1
features_train, features_test, labels_train, labels_test = preprocess(perc = 1)

t0 = time()
clf2 = tree.DecisionTreeClassifier(min_samples_split = 40)
clf2.fit(features_train, labels_train)
print "Fit time: ", time() - t0

t1= time()
pred = clf2.predict(features_test)
print "Predict time: ", time() - t1

from sklearn.metrics import accuracy_score
print "accuracy:", accuracy_score(labels_test, pred)

print "num of features", len(features_train[0])
#########################################################5


