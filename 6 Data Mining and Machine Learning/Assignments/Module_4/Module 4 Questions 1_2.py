# -*- coding: utf-8 -*-
"""
Created on Tue May 13 21:05:05 2025

@author: ntcrw
"""

import pandas  as pd
import math




def manhattan_distance(X1, Y1, X2, Y2):
    
    return int(math.fabs(X1 - X2) + math.fabs(Y1 - Y2))


def  points_in_distance(X1, Y1, X_list, Y_list):
    
    distance_list = []
    
    for i in range(len(X_list)):
        
        distance =  manhattan_distance(X1, Y1, X_list[i], Y_list[i])
        
        distance_list.append(distance)
            
            
    return distance_list   


# Read in the data from the CSV file            
points_df = pd.read_csv("homework_4_dataset.csv")  


# Pre-question work ----------------------------------------------------------
X_values = points_df['X'].to_list()
Y_values = points_df['Y'].to_list() 

print(points_df)

print("\nX values: \n", X_values)
print("\nY values: \n", Y_values)


# -----------------------------------------------------------------------------
# 
# Question 1:
# 
# Using Manhattan Distance, how many points are within distance 20 to point 
# (4, 0)?

X1 = 4 
Y1 = 0
dist = 20

Q1_list = points_in_distance(X1, Y1, X_values, Y_values)

q1_df = points_df.copy()

q1_df["Distance"] = Q1_list


num_points_4_0 = len(q1_df[q1_df['Distance'] <= dist])


print("\n\nNumber of points in ", str(dist), " is: ", num_points_4_0)



# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 2
#
#Using Manhattan Distance, how many points are within distance 100 to 
# point (57, 56)? 

X2 = 57
Y2 = 56
dist2 = 100

Q2_list = points_in_distance(X2, Y2, X_values, Y_values)

q2_df = points_df.copy()

q2_df["Distance"] = Q2_list

num_points_57_56 =len(q2_df[q2_df['Distance'] <= dist2])


print("\n\nNumber of points in ", str(dist), " is: ", num_points_57_56)

# ----------------------------------------------------------------------------
