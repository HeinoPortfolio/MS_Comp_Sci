# -*- coding: utf-8 -*-
"""
Created on Sun May 18 04:12:23 2025

@author: ntcrw
"""

import math
import matplotlib.pyplot as plt
import pandas as pd 

# Methods ---------------------------------------------------------------------


def get_x_values(some_cluster):  
    
    x_values = []

    for index in range(len(some_cluster)):
        
        x_values.append(some_cluster[index][0])
    
    
    return x_values

#------------------------------------------------------------------------------

def get_y_values(some_cluster):  
    
    y_values = []

    for index in range(len(some_cluster)):
        
        y_values.append(some_cluster[index][1])
    
    
    return y_values

#------------------------------------------------------------------------------

def manhattan_distance(p, q):
    
    return math.fabs(p[0] - q[0]) + math.fabs(p[1] - q[1])


#------------------------------------------------------------------------------

def my_distance_min(clust_1, clust_2):
    
    distance = 1000
    
    for p in clust_1:
        for q in clust_2:
            if manhattan_distance(p, q) < distance:
                
                distance = manhattan_distance(p, q)
                
    return distance

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Pre-question tasks ----------------------------------------------------------

# Read in the data from the file. ---------------------------------------------

points_df  = pd.read_csv("cs654_exam1_dataset.csv", header=None)


# Visualize the data ---------------------------------------------------------


cluster_p = [[50, 98], [54, 6], [34, 66]]
cluster_q = [[63, 52], [39, 62], [46, 75]]
cluster_r = [[28, 65], [18, 37], [18, 97]]



# P cluster values ------------------------------------------------------------

x_values_p =  get_x_values(cluster_p)
y_values_p =  get_y_values(cluster_p)

# Q cluster values ------------------------------------------------------------

x_values_q =  get_x_values(cluster_q)
y_values_q =  get_y_values(cluster_q)

# R cluster values ------------------------------------------------------------

x_values_r =  get_x_values(cluster_r)
y_values_r =  get_y_values(cluster_r)


plt.ylim([0,105])
plt.xlim([0,105])


plt.scatter(x_values_p, y_values_p, color="red")
plt.scatter(x_values_q, y_values_q, color="green")
plt.scatter(x_values_r, y_values_r, color="blue")


plt.show()