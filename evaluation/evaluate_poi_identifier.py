#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


from sklearn.tree import DecisionTreeClassifier


dtc1 = DecisionTreeClassifier()
from sklearn.model_selection import train_test_split
labels_train, labels_test, features_train, features_test = \
    train_test_split(labels, features, test_size = 0.3, random_state = 42)
dtc1.fit(features_train, labels_train)
score1 = dtc1.score(features_test, labels_test)
print (score1)

print ("number of labels in the test set = ", len(labels_test))
from numpy import unique
print ("number of unique labels in the test set = ", len(unique(labels_test)))
print ("number of ones labels in the test set = ", sum(i==1.0 for i in labels_test))
labels_predicted = dtc1.predict(features_test)
print ("number of predicted ones labels in the test set = ", sum(i==1.0 for i in labels_predicted))

from sklearn.metrics import precision_score, recall_score

print ("Precision score = ", precision_score(labels_test, labels_predicted))
print ("Recall score = ", recall_score(labels_test, labels_predicted))
