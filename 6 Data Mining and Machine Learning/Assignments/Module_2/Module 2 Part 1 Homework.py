# -*- coding: utf-8 -*-
"""
Created on Mon May 12 02:06:33 2025

@author: ntcrw
"""

import pandas as pd


# read in the CSV file into a dataframe

airline_df = pd.read_csv("cs654_homework2_dataset1.csv")

print(airline_df)

# print (airline_df['ArrDelay'])


# ----------------------------------------------------------------------------
#
# Question 1:
#
# How many rows in this dataset?

print("\n\nQuestion 1: \nNumber of rows in the dataframe: ", len(airline_df))

# -----------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 2:
#
# What is the mean value of column ArrDelay?


mean_arrDelay = airline_df['ArrDelay'].mean()

print(f"\n\nQuestion 2: \nMean of ArrDelay is:  {mean_arrDelay}")

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 3:
#
# What is the median value of column DepDelay?

medianDepDelay = airline_df['DepDelay'].median()

print(f"\n\nQuestion 3: \nMedian of DepDelay is:  {medianDepDelay}")

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 4
#
# For column Origin, which value has the highest frequency?

origin_counts = airline_df['Origin'].value_counts()

origin_df = origin_counts.to_frame()


print(origin_df)



























