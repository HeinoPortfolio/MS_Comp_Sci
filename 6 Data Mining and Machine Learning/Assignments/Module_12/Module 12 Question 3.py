# -*- coding: utf-8 -*-
"""
Created on Thu May 15 18:24:42 2025

@author: ntcrw


Datasets used:

- cs654_module_12_dataset1.csv   (positive reviews) -->     Dataset 1
- cs654_module_12_dataset2.csv   (negative reviews) -->     Dataset 2
- cs654_module_12_dataset3.csv   (stopwords)        -->     Dataset 3    

Perform data cleaning as (Do not mix the order)

   - 1) remove punctuation first

   - 2) remove words contained in dataset 3

   - 3) normalize every word in their lower case


"""
import pandas as pd



# Pre-question tasks ---------------------------------------------------------


# Import cleaned data from dataset 1 -----------------------------------------
dataset_1_df = pd.read_csv("ds1_cleaned.csv", header=None)

cleaned_1 = dataset_1_df.iloc[0, :].tolist()


# Import cleaned data from dataset 2 -----------------------------------------
dataset_2_df = pd.read_csv("ds2_cleaned.csv", header=None)

cleaned_2 = dataset_2_df.iloc[0, :].tolist()

#------------------------------------------------------------------------------
#
# Question 3 
#
# What is the number of common distinct words in dataset 1 and dataset 2?

# Create a set of the two lists ----------------------------------------------


combined_d1_d2 = cleaned_1 + cleaned_2

#print(combined_d1_d2)

common_distinct = set(combined_d1_d2)














