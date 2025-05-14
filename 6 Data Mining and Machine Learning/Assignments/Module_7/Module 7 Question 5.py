# -*- coding: utf-8 -*-
"""
Created on Wed May 14 14:22:28 2025

@author: ntcrw


Note: will use cs654_homework7_train_30.csv and cs654_homework7_train_30_labels.csv 
to train a scikit-learn KNeighborsClassifier, and test its performance using 
cs654_homework7_test_10.csv and cs654_homework7_test_10_labels.csv.

"""

import pandas as pd
import warnings

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# Pre-question tasks ----------------------------------------------------------

warnings.filterwarnings("ignore")

# Read in the training data points to a list and transform to a list

training_data_points = pd.read_csv("cs654_homework7_train_30.csv", 
                                   header=None).values.tolist()
training_data_labels = pd.read_csv("cs654_homework7_train_30_labels.csv", 
                                   header=None).values.tolist()


# Read in the test data items and transform to a list

test_data_points = pd.read_csv("cs654_homework7_test_10.csv", 
                               header=None).values.tolist()
test_data_labels = pd.read_csv("cs654_homework7_test_10_labels.csv", 
                               header=None).values.tolist()


# Check the length
#print("\nTraining data length: ", len(training_data_points))
#print("Training data lable length: ", len(training_data_labels))

#print("\nTest data length: ", len(training_data_points))
#print("Test data lable length: ", len(test_data_labels))


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 5:
#
# When K = 9, what is the prediction accuracy of the test data? 
#

# Create the KNN classifier ---------------------------------------------------

knn_classifier_1 = KNeighborsClassifier(n_neighbors=9)


# Train the model with the training data (learn) ------------------------------

knn_classifier_1.fit(training_data_points, training_data_labels)

# Make a prediction using the test data points --------------------------------

predicted_labels = knn_classifier_1.predict(test_data_points)


print("\nPredicted labels:", predicted_labels)


# Compute the accuracy of the model -------------------------------------------

accuracy = accuracy_score(test_data_labels, predicted_labels)

print("\nThe accuracy of the model with K=9 was: ", accuracy)



