# -*- coding: utf-8 -*-
"""
Created on Tue May 13 21:05:05 2025

@author: ntcrw
"""

import pandas  as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



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


points_list = points_df.values.tolist()


pts = np.array(points_list)

# Visualize the points

sns.scatterplot(
    
    x='X',
    y='Y',
    data=points_df
    
    )

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 1 
#
# Using Manhattan Distance, how many points are within distance 20 to point 
# (4, 0)?

# Add the point in question to the plot
sns.scatterplot(
    
    x='X',
    y='Y',
    data=points_df
    
    )
plt.scatter(4, 0, color='r')
plt.show()


X1 = 4 
Y1 = 0
dist = 20

Q1_list = points_in_distance(X1, Y1, points_df['X'], points_df['Y'])

q1_df = points_df.copy()

q1_df["Distance_4_0"] = Q1_list


num_points_4_0 = len(q1_df[q1_df['Distance_4_0'] <= dist])


print("\n\nNumber of points in ", str(dist), " is: ", num_points_4_0)


results_df_4_0 = q1_df[q1_df['Distance_4_0'] <= dist]

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 2
#
# Using Manhattan Distance, how many points are within distance 100 to 
# point (57, 56)? 
#
sns.scatterplot(
    
    x='X',
    y='Y',
    data=points_df
    
    )
plt.scatter(56, 57, color='g')
plt.show()


X2 = 57
Y2 = 56
dist2 = 100

Q2_list = points_in_distance(X2, Y2, points_df['X'], points_df['Y'])

q2_df = points_df.copy()

q2_df["Distance_56_57"] = Q2_list

num_points_57_56 =len(q2_df[q2_df['Distance_56_57'] <= dist2])


print("\n\nNumber of points in ", str(dist), " is: ", num_points_57_56)

results_df_57_56 = q2_df[q2_df['Distance_56_57'] <= dist]


# add labels list to the data frame
distance_56_57 = []


for item in q2_df['Distance_56_57'].values.tolist():
    
    #print(item)
    if item <= dist2:
        distance_56_57.append(1)
    else:
        distance_56_57.append(0)
    

q2_df['100_Distance'] = distance_56_57 

sns.scatterplot(
    
    x='X',
    y='Y',
    data=q2_df,
    hue='100_Distance'
    
    )

plt.scatter(56, 57, color='g')
plt.show()





