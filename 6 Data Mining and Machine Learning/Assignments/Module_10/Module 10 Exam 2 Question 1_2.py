# -*- coding: utf-8 -*-
"""
Created on Mon May 19 03:53:10 2025

@author: ntcrw

Note:
    
    This exam consists of two data files. 
    
    - cs654_exam2_dataset1.csv
    - cs654_exam2_dataset2.csv

"""

import pandas as pd
import numpy as np

import warnings

# Pre-question tasks ----------------------------------------------------------

warnings.filterwarnings('ignore')

# Read in dataset 1 -----------------------------------------------------------
dataset_1_df = pd.read_csv("cs654_exam2_dataset1.csv")

# Read in dataset 2 -----------------------------------------------------------

dataset_2_df = pd.read_csv("cs654_exam2_dataset2.csv")


# Verify contents have been read in to the dataframes -------------------------
# show the dataframe ----------------------------------------------------------

print("Contents of dataframe 1: \n",dataset_1_df.head())
print("Contents of dataframe 2: \n",dataset_1_df.head())

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 1:
#
# How many distinct labels( in label column) in the dataset1 and dataset2?
#

# Extract the unique values from the label column dataset 1--------------------

distinct_values_1 = dataset_1_df['label'].unique()

# Extract the unique values from the label column in dataset 2 ----------------

distinct_values_2 = dataset_2_df['label'].unique()

# Create a set of labels of both sets -----------------------------------------

total_labels = np.concatenate(( distinct_values_1 ,distinct_values_2))

total_distinct = set(total_labels)

# Show the result -------------------------------------------------------------

print("\n\n\nQuestion 1: \n\nTotal distinct labels:  ", len(total_distinct))


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 2:
#
# How many rows in dataset 1
#


#  Compute the number of rows in the first dataset ---------------------------

 
print("\n\n\nQuestion 2: \n\nThe number of rows in dataset 1[using len()]: ", 
      len(dataset_1_df))


# using the shape attribute ---------------------------------------------------
print("\nNumber of rows [using .shape]: ", dataset_1_df.shape[0])






















