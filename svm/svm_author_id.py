#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
###
from sklearn.svm import SVC
#%%
print ("---linear classifier, full training set ---")

clf = SVC(kernel="linear")

t0 = time()
clf.fit (features_train, labels_train)
print ("training time: ", round(time()-t0, 3)," s")

t1 = time()
labels_predicted = clf.predict (features_test)
print ("prediction time: ", round(time()-t1, 3)," s")

from sklearn.metrics import accuracy_score

acc_score = accuracy_score(labels_predicted, labels_test)
print (acc_score)

#%% only reduce number of labels
print ("---linear classifier, 1% training set ---")

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
#%% test classifier, because it is fast
clf1 = SVC(kernel="linear")

t0 = time()
clf1.fit (features_train, labels_train)
print ("training time: ", round(time()-t0, 3)," s")

t1 = time()
labels_predicted = clf1.predict (features_test)
print ("prediction time: ", round(time()-t1, 3)," s")

acc_score = accuracy_score(labels_predicted, labels_test)
print (acc_score)

#print labels_predicted [:10]


#%%

print ("---rbf classifier, 1% training set ---")

clf2 = SVC(kernel="rbf")

t0 = time()
clf2.fit (features_train, labels_train)
print ("training time: ", round(time()-t0, 3)," s")

t1 = time()
labels_predicted = clf2.predict (features_test)
print ("prediction time: ", round(time()-t1, 3)," s")

acc_score = accuracy_score(labels_predicted, labels_test)
print (acc_score)

print ("---rbf classifier, 1% training set, C=10 ---")

clf3 = SVC(kernel="rbf", C=10)

t0 = time()
clf3.fit (features_train, labels_train)
print ("training time: ", round(time()-t0, 3)," s")

t1 = time()
labels_predicted = clf3.predict (features_test)
print ("prediction time: ", round(time()-t1, 3)," s")

acc_score = accuracy_score(labels_predicted, labels_test)
print (acc_score)

print ("---rbf classifier, 1% training set, C=100 ---")

clf4 = SVC(kernel="rbf", C=100)

t0 = time()
clf4.fit (features_train, labels_train)
print ("training time: ", round(time()-t0, 3)," s")

t1 = time()
labels_predicted = clf4.predict (features_test)
print ("prediction time: ", round(time()-t1, 3)," s")

acc_score = accuracy_score(labels_predicted, labels_test)
print (acc_score)


print ("---rbf classifier, 1% training set, C=1000 ---")

clf5 = SVC(kernel="rbf", C=1000)

t0 = time()
clf5.fit (features_train, labels_train)
print ("training time: ", round(time()-t0, 3)," s")

t1 = time()
labels_predicted = clf5.predict (features_test)
print ("prediction time: ", round(time()-t1, 3)," s")

acc_score = accuracy_score(labels_predicted, labels_test)
print (acc_score)

print ("---rbf classifier, 1% training set, C=10000 ---")

clf6 = SVC(kernel="rbf", C=10000)

t0 = time()
clf6.fit (features_train, labels_train)
print ("training time: ", round(time()-t0, 3)," s")

t1 = time()
labels_predicted = clf6.predict (features_test)
print ("prediction time: ", round(time()-t1, 3)," s")

acc_score = accuracy_score(labels_predicted, labels_test)
print (acc_score)

#%%from here
print ("---rbf classifier, full training set, C=10000 ---")

print("preproceccing training set")
features_train, features_test, labels_train, labels_test = preprocess()

clf7 = SVC(kernel="rbf", C=10000)

t0 = time()
clf7.fit (features_train, labels_train)
print ("training time: ", round(time()-t0, 3)," s")

t1 = time()
labels_predicted = clf7.predict (features_test)
print ("prediction time: ", round(time()-t1, 3)," s")

acc_score = accuracy_score(labels_predicted, labels_test)
print (acc_score)

import collections
cnt = collections.Counter(labels_predicted)
print (cnt)
#print ("number of predicted mails of chris: ", labels_predicted.count(1))

#########################################################


