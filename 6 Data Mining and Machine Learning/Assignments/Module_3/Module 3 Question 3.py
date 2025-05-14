# -*- coding: utf-8 -*-
"""
Created on Tue May 13 17:06:12 2025

@author: ntcrw
"""

from sklearn.preprocessing import MinMaxScaler

import pandas as pd
import numpy as np

#-----------------------------------------------------------------------------
# Read in the file

sales_df = pd.read_csv("cs654_homework_3_dataset.csv")

def min_max(global_data):
    
   global_sales_data_sorted = np.sort(global_data)


   #print(global_sales_data_sorted)


   # Reshape the array
   global_sales_data_sorted = global_sales_data_sorted.reshape(-1, 1)
   
   
   # Create the scaler
   scaler_mm = MinMaxScaler()
   mm_model = scaler_mm.fit(global_sales_data_sorted)

   # Transform the data 
   global_sales_data_scaled = mm_model.transform(global_sales_data_sorted)


   return np.round(global_sales_data_scaled, decimals=2) 


def minmax_formula(global_data):
    
    global_sales_list = global_data.tolist()
    
    
    # Sort the list
    global_sales_list.sort()
    
    # Extract the minimum and maximum values in the list of sorted numbers

    min_val = global_sales_list[0]
    max_val = global_sales_list[-1]
    
    normalized_list = []

    for element in global_sales_list:
       
       normalized_list.append(round((element - min_val) / (max_val - min_val), 2))
    
    return normalized_list

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 3 
#
# After applying min-max normalization on Global_Sales attribute values, 
# how many of them are more than 0.5 ?


# Extract the column from the dataframe

global_sales_data =  sales_df['Global_Sales']


# Compute the normalized form using formula
 
normalized_form = minmax_formula(global_sales_data)


count_gt_05 = 0  


for item in normalized_form:
    
    if item > 0.5:
        
        count_gt_05 = count_gt_05 + 1
        

print("\n\n\n The number of values with values greater than 0.5 is (by formula)): ",
      count_gt_05)
       
# ---------------------------------------------------------------------------- 
# Using MinMax scaler


# Call the method
# Extract the data from the column

global_sales_data_np =  sales_df['Global_Sales'].to_numpy()

scaled_data_mm = min_max(global_sales_data_np)


# Count the values in the list that are less than 0.5


count_lt_05 = 0  


for item in scaled_data_mm:
    
    if item > 0.5:
        
        count_lt_05 = count_lt_05 + 1
        

print("\n\n\n The number of values with values less than 0.5 is: ",
      count_lt_05)



# Create a dataframe for the normalized values

normalized_df = pd.DataFrame(normalized_form, columns=["Formula"])

# Add the minmax values to the data frame
normalized_df['MinMax'] = scaled_data_mm


# Show the values in dataframe for comparison
print(normalized_df)

# -----------------------------------------------------------------------------
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


