# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:16:54 2024

@author: ntcrw

Notes:
    1)
    2) 
"""

import numpy as np
from sklearn import tree
import matplotlib.pyplot as plot
import pandas as pd


# ============================================================================
# Question 1 
#
# What is the size of the dataset training_digits.csv?
#
# ============================================================================

# read in the training digits data set
# using pandas

training_data_df = pd.read_csv('training_digits.csv')
#print("Size of training dataset: ", len(training_data_df))


# =============================================================================

# ============================================================================
# Question 2 
#
# What is the size of the dataset test_digits.csv?
#
# ============================================================================

# read in the trest digits data set
# using pandas

test_data_df = pd.read_csv('test_digits.csv')
#print("Size of test dataset: ", len(test_data_df))

# =============================================================================

# =============================================================================
# Question 4
# In the test data, i.e., test_digits.csv, which digit has the highest 
# number of rows?
#
# =============================================================================

# Columns of the dataframe

#print(test_data_df.columns)

labels = test_data_df.loc[ : , 'label']

# Create a set of unique values.
unique_keys = labels.unique()

# Create a dictionary with the unique lables.

label_count_dict = dict.fromkeys(unique_keys, 0) 
#print(label_count_dict.keys())

# iterate through the labels and update the count
for label in labels:
   
   label_count_dict[label] += 1 

# find the maximum in dictionary
maximum_res = max(label_count_dict, key=label_count_dict.get)

#print("Digit with highest number of rows: ", maximum_res)

# =============================================================================


# =============================================================================
# Question 5
#
# In the test data, i.e., test_digits.csv, which digit has the lowest
# number of rows?
#
# =============================================================================
# find the maximum in dictionary
minimum_res = min(label_count_dict, key=label_count_dict.get)

#print("Digit with least number of rows: ", minimum_res)


# ============================================================================
# Question 6
#
# Which one of the following descriptions is correct (on test data only)?
#
# =============================================================================

# ????????










































