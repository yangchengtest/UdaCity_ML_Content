#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

clf= GaussianNB()
predict = clf.fit(features_train, labels_train).predict(features_test)
uncurrent = 0
print len(predict)
for index in range(len(predict)):
    if (predict[index]!=labels_test[index]):
        uncurrent=uncurrent+1
print uncurrent        
print float(uncurrent)/len(predict)
#########################################################


