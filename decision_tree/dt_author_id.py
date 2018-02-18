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
from sklearn.tree import DecisionTreeClassifier

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
clf = DecisionTreeClassifier(min_samples_split=40)
predict = clf.fit(features_train, labels_train).predict(features_test)
uncurrent = 0
print len(predict)
print len(features_train[0])
for index in range(len(predict)):
    if (predict[index]!=labels_test[index]):
        uncurrent=uncurrent+1
print uncurrent        
print 1-float(uncurrent)/len(predict)


#########################################################
### your code goes here ###


#########################################################


