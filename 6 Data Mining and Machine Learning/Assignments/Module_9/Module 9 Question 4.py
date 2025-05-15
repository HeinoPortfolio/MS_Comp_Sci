# -*- coding: utf-8 -*-
"""
Created on Thu May 15 00:48:58 2025

@author: ntcrw


Datasets used:
    
    - cs654_homework9_train_30.csv              -->         Dataset 1
    - cs654_homework9_train_30_labels.csv       -->         Dataset 2  
    - cs654_homework9_test_10.csv               -->         Dataset 3  
    - cs654_homework9_test_10_labels.csv        -->         Dataset 4

"""

import pandas as pd
import warnings

from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression


# Pre-question Tasks ----------------------------------------------------------

warnings.filterwarnings("ignore")

# Read in the training data points to a list and transform to a list ----------
training_data_points = pd.read_csv("cs654_homework9_train_30.csv", 
                                   header=None).values.tolist()

training_data_labels = pd.read_csv("cs654_homework9_train_30_labels.csv", 
                                   header=None).values.tolist()


# Read in the test data items and transform to a list -------------------------

test_data_points = pd.read_csv("cs654_homework9_train_30.csv", 
                               header=None).values.tolist()

test_data_labels = pd.read_csv("cs654_homework9_train_30_labels.csv", 
                               header=None).values.tolist()

# Check the length ------------------------------------------------------------

#print("\nTraining data length: ", len(training_data_points))
#print("Training data lable length: ", len(training_data_labels))

#print("\nTest data length: ", len(test_data_points))
#print("Test data lable length: ", len(test_data_labels))


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 4:
#
# Use dataset 1 and dataset 2 to construct a LogisticRegression classifier as 
# demonstrated in the class sample. 
#
# Use dataset 1 and dataset 2 to test the classifier. 
#
# What is its accuaracy? 
#


# Create the CategoricalNB ----------------------------------------------------

lr_clf = LogisticRegression(random_state=77)


# Train the model with the training data (learn) ------------------------------

lr_clf.fit(training_data_points, training_data_labels)


# Compute the model's accuracy ------------------------------------------------

predicted_labels = lr_clf.predict(test_data_points)


# Output the accuracy results -------------------------------------------------

accuracy = accuracy_score(test_data_labels, predicted_labels)

accuracy_lr = lr_clf.score(test_data_points, test_data_labels)


# Print out the results -------------------------------------------------------

print("\nQuestions 4: \nThe accuracy of the model was (accuracy_score())): ",
      accuracy)

print("\nQuestions 4: \nThe accuracy of the model (using score()) was: ",
      accuracy_lr)

