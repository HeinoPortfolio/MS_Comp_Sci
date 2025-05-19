"""
Created on Mon May 19 03:53:10 2025

@author: ntcrw

Note:
    
    This exam consists of two data files. 
    
    - cs654_exam2_dataset1.csv
    - cs654_exam2_dataset2.csv
    
    This file will create a Decision Tree classifier 

"""

import pandas as pd
import warnings

from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

#------------------------------------------------------------------------------
# Pre-question tasks ----------------------------------------------------------

warnings.filterwarnings('ignore')

# Read in dataset 1 -----------------------------------------------------------
dataset_1_df = pd.read_csv("cs654_exam2_dataset1.csv")

# Read in dataset 2 -----------------------------------------------------------

dataset_2_df = pd.read_csv("cs654_exam2_dataset2.csv")


# Verify contents have been read in to the dataframes -------------------------
# show the dataframe ----------------------------------------------------------

#print("Contents of dataframe 1: \n",dataset_1_df.head())
#print("Contents of dataframe 2: \n",dataset_1_df.head())

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Extract the features to be used for training the model ---------------------- 
# Will use all columns except the first column which contains the labels ------


X_train = dataset_1_df.iloc[:, 1:].to_numpy()

# Check the shape of the values in X_train ------------------------------------
#print("Shape of X train: ", X_train.shape)


Y_train = dataset_1_df.iloc[:, 0].to_numpy()
#print("Shape of y train: ", Y_train.shape)


#------------------------------------------------------------------------------
# Extract the features that will be used to test the model---------------------
# Will use all columns except the first column which contains the labels ------

X_test = dataset_2_df.iloc[:, 1:].to_numpy()

# Check the shape of the values in X_test ------------------------------------
#print("Shape of X test: ", X_test.shape)

Y_test = dataset_2_df.iloc[:, 0].to_numpy()

# Check the shape of the values in Y_test ------------------------------------
#print("Shape of y test: ", Y_test.shape)


# -----------------------------------------------------------------------------
# Create the GaussianNB classifier -----------------------------------------

gnb_clf = GaussianNB()


#------------------------------------------------------------------------------
# Train the model with dataset 1 test data ------------------------------------

gnb_clf.fit(X_train, Y_train)


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 5:
#
# Use dataset 1 to train a scikit learn GaussianNB classifier. Test the 
# constructed classifier on dataset 2. 
#
# What is the accuracy?
#

# Make a prediction using the data in dataset 2 -- the test data --------------
predicted_labels = gnb_clf.predict(X_test) 


#------------------------------------------------------------------------------
# Compute the accuracy scores -------------------------------------------------

accuracy = accuracy_score(Y_test, predicted_labels)

accuracy_score = gnb_clf.score(X_test, Y_test)

# Show the accuracy of the model ---------------------------------------------
 
print("\n\nQuestion 5: \nAccuracy [using accuracy_score]:", accuracy)
print("\n\nQuestion 5: \nAccuracy [using .score]:", accuracy_score)
















 





