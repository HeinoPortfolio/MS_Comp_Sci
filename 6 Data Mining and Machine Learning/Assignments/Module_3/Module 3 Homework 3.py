# -*- coding: utf-8 -*-
"""
Created on Mon May 12 03:26:46 2025

@author: ntcrw
"""

import pandas as pd


# read in the file

sales_df = pd.read_csv("cs654_homework_3_dataset.csv")

# verify the dataframe
print(sales_df)

# ----------------------------------------------------------------------------
# 
# Question 1:
#
# How many distinct values in the Platform attribute?

import copy 

# unique_platform = sales_df['Platform'].unique()

#print("\n Unique values of the Platform attribute are: ", sales_df['Platform'].unique())

#print("\n\nQuestion 1: \n\nNumber of distinct values in 'Platform' attribute: ", 
#      len(pd.unique(sales_df['Platform'])))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 2:
#
# In the Release Date column, how many newer values in the Release_Date
# column are there?

#new_count = len(sales_df[sales_df['Release_Date'] == 'newer'])

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 3 
#
# After applying min-max normalization on Global_Sales attribute values, 
# how many of them are more than 0.5 ?


# Extract the column from the dataframe

"""
global_sales_data =  sales_df['Global_Sales']

#print(type(global_sales_data))

global_sales_list = global_sales_data.tolist()

#print(type(global_sales_list))
#print(global_sales_list)

# Sort the list
global_sales_list.sort()

#print("\n\n\n",global_sales_list)

# Extract the minimum and maximum values in the list of sorted numbers

min_val =  global_sales_list[0]
max_val = global_sales_list[-1]


#print("min value:  ", min_val, "By min(): ", min(global_sales_list))
#print("max value:  ", max_val, "By max(): ", max(global_sales_list))

# compute the min max values

normalized_list = []

for element in global_sales_list:
    
   #print(round((element - min_val) / (max_val - min_val), 4))
   
   normalized_list.append(round((element - min_val) / (max_val - min_val), 4))
   
# Count the values in the list that are more than 0.5


count_gt_05 = 0  


for item in normalized_list:
    
    if item > 0.5:
        
        count_05 = count_05 + 1
        

print("\n\n\n The number of values with values greater than 0.5 is: ",
      count_gt_05)
    
 """   
# -----------------------------------------------------------------------------
#
# Question 4 
#
# After applying min-max normalization on EU_Sales column values, how many of 
# them are less than 0.5?


eu_sales_data =  sales_df['EU_Sales']

eu_sales_list = eu_sales_data.tolist()


eu_sales_list.sort()

print(eu_sales_list)

min_val =  min(eu_sales_list)
max_val = max(eu_sales_list)

normalized_list = []

for element in eu_sales_list:
    
   
   normalized_list.append(round((element - min_val) / (max_val - min_val), 4))



count_lt_05 = 0

for item in normalized_list:
    
    if item < 0.5:
        
        count_lt_05 = count_lt_05 + 1
        

print("\n\n\n The number of values with values less than 0.5 is: ",
      count_lt_05)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 5
#
# If we use the normalized(min-max)Global_sales and EU_sales attributes with 
# equal weights (0.5 for each), what is the distance between the 1st row 
# (index 0) and the 2nd row(index 1)? Choose the best answer


# Need to compute the distances and then compute the distances for the 
# two columns 








# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 6
#
# If we use the normalized(min-max) Global_sales and EU_sales attribute 
# with equal weights(0.5), what is the distance between the 1st row(index 0) 
# and the 100th row(index 99)? Choose the best answer.

























