# -*- coding: utf-8 -*-
"""
Created on Fri May 16 18:11:11 2025

@author: ntcrw
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier

import numpy as np
import pandas as pd



# read in the data from the CSV files into a dataframe

# Training data load ---------------------------------------------------------- 

train_30_data_df = pd.read_csv("cs654_homework14_train_30.csv", header=None)
train_30_labels_df =  pd.read_csv("cs654_homework14_train_30_labels.csv",
                                  header=None)

# Testing data load -----------------------------------------------------------

test_10_data_df = pd.read_csv("cs654_homework14_test_10.csv", header=None)
test_10_labels_df =  pd.read_csv("cs654_homework14_test_10_labels.csv",
                                 header=None)



#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 5:
#
# Use dataset1 and dataset 2 to train a scikit learn MLP Classifier and test 
# the neural network on dataset 3 and dataset 4. If we specify the following: 
# logistic activation, what is the accuracy?
#


# Convert the dataframes to a numpy array -------------------------------------

X_train = train_30_data_df.to_numpy()
y_train = train_30_labels_df.to_numpy()


X_test = test_10_data_df.to_numpy()
y_test = test_10_labels_df.to_numpy()

# Create the MLPClassifer -----------------------------------------------------

mlp_clf = MLPClassifier(activation='relu', max_iter=1000, random_state=42)


# Train the model with training data ------------------------------------------

mlp_clf.fit(X_train, y_train)


# Generate the accuracy score -------------------------------------------------

accuracy_score_re = mlp_clf.score(X_test, y_test)

# Print the results of the model ----------------------------------------------

print("\nQuestion 6: \n\nUsing 'relu', the accuracy of the model was: ",
      accuracy_score_re)

