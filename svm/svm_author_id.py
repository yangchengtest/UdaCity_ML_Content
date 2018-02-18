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
from sklearn.svm import SVC

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf= SVC(kernel="linear")
predict = clf.fit(features_train, labels_train).predict(features_test)
uncurrent = 0
print len(predict)
for index in range(len(predict)):
    if (predict[index]!=labels_test[index]):
        uncurrent=uncurrent+1
print uncurrent        
print float(uncurrent)/len(predict)


#########################################################
### your code goes here ###

#########################################################


