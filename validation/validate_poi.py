#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(features, labels)
score = dtc.score(features, labels)
print (score)

dtc1 = DecisionTreeClassifier()
from sklearn.model_selection import train_test_split
labels_train, labels_test, features_train, features_test = \
    train_test_split(labels, features, test_size = 0.3, random_state = 42)
dtc1.fit(features_train, labels_train)
score1 = dtc1.score(features_test, labels_test)
print (score1)
