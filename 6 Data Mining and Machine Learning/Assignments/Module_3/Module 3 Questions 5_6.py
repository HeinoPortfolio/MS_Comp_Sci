# -*- coding: utf-8 -*-
"""
Created on Tue May 13 17:07:43 2025

@author: ntcrw
"""

from sklearn.preprocessing import MinMaxScaler
import math
import pandas as pd
import numpy as np


# Methods for questions 5 and 6 ----------------------------------------------

def distance_matrix(normalized_list):
    
    distance_matrix_list = []
    
    for i in range(len(normalized_list)):
        
        distance_row = []
    
        for j in range(len(normalized_list)):
        
           # print(round(math.fabs(normalized_list[i] - normalized_list[j]), 2), end="\t")
        
            distance_row.append(round(math.fabs(normalized_list[i] - normalized_list[j]), 2))
   
        distance_matrix_list.append(distance_row)
    
    
    return distance_matrix_list

#------------------------------------------------------------------------------
def final_distance_matrix(distance_matrix_global_sales,  distance_matrix_eu_sales):
    
   distance_matrix_final = []
     
   for i in range(len(distance_matrix_list_gs)):
       
       distance_row = []
         
       for j in range(len(distance_matrix_list_gs[i])):
           
           distance =(distance_matrix_list_gs[i][j] * 0.5 + 
                        distance_matrix_list_eu[i][j] * 0.5 )
        
           distance_row.append(round(distance, 2))
         
       distance_matrix_final.append(distance_row)
       
   return distance_matrix_final

# -----------------------------------------------------------------------------

def min_max(some_data):

   # Create the scaler
   scaler_mm = MinMaxScaler()
   mm_model = scaler_mm.fit(some_data)

   # Transform the data 
   data_scaled = mm_model.transform(some_data)


   return np.round(data_scaled, decimals=2) 

# -----------------------------------------------------------------------------

def minmax_formula(some_data):
    
    data_list = some_data.tolist()
    
    # Extract the minimum and maximum values in the list of sorted numbers

    min_val = min(some_data)
    max_val = max(some_data)
    
    normalized_list = []

    for element in data_list:
       
       normalized_list.append(round((element - min_val) / (max_val - min_val), 2))
    
    return normalized_list


# Pre-question work -----------------------------------------------------------

data_df = pd.read_csv("cs654_homework_3_dataset.csv")
global_sales = pd.DataFrame(data_df['Global_Sales'])
global_sales_list = data_df['Global_Sales']


#global_sales_norm =  min_max(global_sales)

global_sales_norm_form =  minmax_formula(global_sales_list)


# get EU_sales data -----------------------------------------------------------
eu_sales_list = data_df['EU_Sales']
eu_sales_norm_form = minmax_formula(eu_sales_list)

# View each side-by-side in a dataframe
# Create a dataframe for the normalized values -------------------------------
#normalized_df = pd.DataFrame(global_sales_norm_form, columns=["Formula"])
# Add the minmax values to the data frame
#normalized_df['MinMax'] = global_sales_norm_form
# Show the values in dataframe for comparison
#print(normalized_df)


# Call the distance matrix function -------------------------------------------
distance_matrix_list_gs = distance_matrix(global_sales_norm_form)

#print(distance_matrix)

# Convert to a dataframe 
distance_matrix_df_GS = pd.DataFrame(distance_matrix_list_gs)
#print(distance_matrix_df_GS)



# Call the distance matrix function -------------------------------------------
distance_matrix_list_eu = distance_matrix(eu_sales_norm_form)

# Convert to a dataframe 
distance_matrix_df_EU = pd.DataFrame(distance_matrix_list_eu)
#print(distance_matrix_df_EU)

  
# View the contents of the distance lists -------------------------------------
  
# Contents of the global sales distance list  
#print(distance_matrix_list_gs)
#print(type(distance_matrix_list_gs))

# Contents of the global sales distance list
#print(distance_matrix_list_eu)
#print(type(distance_matrix_list_eu))


# Get the final distance matrix based on weights
# compute the final distance matrix based on weights 

# Call the final distance method wih weights
final_distance_list = final_distance_matrix(distance_matrix_list_gs,  
                                            distance_matrix_list_eu)


# Convert to dataframe

final_distance_df = pd.DataFrame(final_distance_list)



































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