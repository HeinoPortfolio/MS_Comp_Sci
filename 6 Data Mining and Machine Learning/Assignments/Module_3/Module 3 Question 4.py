# -*- coding: utf-8 -*-
"""
Created on Tue May 13 18:17:25 2025

@author: ntcrw
"""

from sklearn.preprocessing import MinMaxScaler
import copy
import pandas as pd
import numpy as np


def min_max(eu_data):
    
   eu_data_sorted = np.sort(eu_data)


   # Reshape the array
   eu_sorted = eu_data_sorted.reshape(-1, 1)
   
   
   # Create the scaler
   scaler_mm = MinMaxScaler()
   mm_model = scaler_mm.fit(eu_sorted)

   # Transform the data 
   eu_data_scaled = mm_model.transform(eu_sorted)


   return np.round(eu_data_scaled, decimals=2) 


def minmax_formula(eu_data):
    
    eu_sales_list = eu_data.tolist()
    
    eu_sales_list.sort()
    
    # Extract the minimum and maximum values in the list of sorted numbers

    min_val = eu_sales_list[0]
    max_val = eu_sales_list[-1]
    
    normalized_list = []

    for element in eu_sales_list:
       
       normalized_list.append(round((element - min_val) / (max_val - min_val), 2))
    
    return normalized_list


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 4 
#
# After applying min-max normalization on EU_Sales column values, how many of 
# them are less than 0.5?

sales_df = pd.read_csv("cs654_homework_3_dataset.csv")


eu_sales_data =  sales_df['EU_Sales']


normalized_list_form =  minmax_formula(eu_sales_data)

normalized_list_mm = min_max(eu_sales_data)

count_lt_05 = 0

for item in normalized_list_form:
    
    if item < 0.5:
        
        count_lt_05 = count_lt_05 + 1
        

print("\n\n\n The number of values with values less than 0.5 is (Formula)): ",
      count_lt_05)

count_lt_05 = 0

for item in normalized_list_form:
    
    if item < 0.5:
        
        count_lt_05 = count_lt_05 + 1
        

print("\n\n\n The number of values with values less than 0.5 is (MinMax)): ",
      count_lt_05)




# Create a dataframe for the normalized values

normalized_df = pd.DataFrame(normalized_list_form, columns=["Formula"])

# Add the minmax values to the data frame
normalized_df['MinMax'] = normalized_list_mm


# Show the values in dataframe for comparison
print(normalized_df)




