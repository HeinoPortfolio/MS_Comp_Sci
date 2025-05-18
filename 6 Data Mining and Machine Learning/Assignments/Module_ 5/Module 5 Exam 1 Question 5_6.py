# -*- coding: utf-8 -*-
"""
Created on Sun May 18 00:30:16 2025

@author: ntcrw
"""

import math
import numpy as np
import pandas as pd 

from sklearn.preprocessing import MinMaxScaler



# Methods --------------------------------------------------------------------

def min_max_formula(list_values): 
    
    max_v= max(list_values)

    min_v = min(list_values)
    
    val_norm = [] 
    
    for val in list_values: 
        
        val_norm.append(round((val - min_v)/ (max_v - min_v), 2))
    
    return val_norm

# -----------------------------------------------------------------------------

def distance_matrix(normalized_list):
    
    distance_matrix_list = []
    
    for i in range(len(normalized_list)):
        
        distance_row = []
    
        for j in range(len(normalized_list)):
        
            distance_row.append(round(math.fabs(normalized_list[i] - normalized_list[j]), 2))
            
        distance_matrix_list.append(distance_row)
    
    return distance_matrix_list

#-----------------------------------------------------------------------------

def final_distance_matrix(distance_matrix_1,  distance_matrix_2): 
    
    distance_matrix_final = []

    for i in range(len(distance_matrix_1)):
    
        distance_row = []
    
        for j in range(len(distance_matrix_1[i])):
        
            distance =(distance_matrix_1[i][j] * 0.5 + 
                       distance_matrix_2[i][j] * 0.5)
        
            distance_row.append(round(distance, 2))
    
        distance_matrix_final.append(distance_row)
    
    return distance_matrix_final
    
#------------------------------------------------------------------------------

    
#------------------------------------------------------------------------------
# Pre-question tasks ----------------------------------------------------------
# -----------------------------------------------------------------------------

# Read the data into a dataframe ---------------------------------------------

points_df = pd.read_csv("cs654_exam1_dataset.csv", header=None)


# Extract the x-values from the dataframe -------------------------------------

X_values = points_df.iloc[:, 0].to_numpy()

# Extract the y-values from the dataframe -------------------------------------

Y_values = points_df.iloc[:, 1].to_numpy()


# -----------------------------------------------------------------------------
# Normalize the points in X and Y ---------------------------------------------
#------------------------------------------------------------------------------

# Normalize the x values ------------------------------------------------------

x_norm =  min_max_formula(X_values)


# Normalize the y values ------------------------------------------------------

y_norm = min_max_formula(Y_values)


# Create the distance vectors for the normalized  X and Y values --------------

distance_x = distance_matrix(x_norm)


# Convert to a dataframe to visualize the matrix ------------------------------
 
distance_matrix_x_df = pd.DataFrame(distance_x)



# Create the distance vectors for the normalized Y values ---------------------
distance_y = distance_matrix(y_norm)


# # Convert to a dataframe to visualize the matrix ----------------------------
distance_matrix_y_df = pd.DataFrame(distance_y)


# Compute the final distance matrix using the weights -------------------------


final_distance_matrix_results =  final_distance_matrix(distance_x,
                                               distance_y)



#------------------------------------------------------------------------------
#
# Question 5 
#
# Use cs654_exam1_dataset.csv and normalize X and Y the values using 
# Min-Max normalization, compute the distances using Manhattan distance and 
# equal weights(0.5 for X and 0.5 for Y).
#
# What is the distance between 
# point 0 ([50,98]) and point 18([41,79])?
# 


# Visualizee the final distance matrix ----------------------------------------

final_distance_matrix_df = pd.DataFrame(final_distance_matrix_results)


# Results of the distance matrix ----------------------------------------------

print("Question 5:  \n The value is: ", final_distance_matrix_df.iloc[0, 18])


#------------------------------------------------------------------------------
#
# Question 6
#
# Use cs654_exam1_dataset.csv and normalize X and Y the values using 
# Min-Max normalization, compute the distances using Manhattan distance and 
# equal weights(0.5 for X and 0.5 for Y), what is the distance between 
# point 8([18,97]) and point 11([91,78])? 
#
 
print("Question 6:  \n The value is: ", final_distance_matrix_df.iloc[8, 11])






