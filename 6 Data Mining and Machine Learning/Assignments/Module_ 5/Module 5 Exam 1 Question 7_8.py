# -*- coding: utf-8 -*-
"""
Created on Sun May 18 02:28:26 2025

@author: ntcrw
"""

import math
import matplotlib.pyplot as plt
import pandas as pd 


#------------------------------------------------------------------------------

def distance(p, q):
    
    return int(math.fabs(p[0] - q[0]) + math.fabs(p[1]-q[1]))

# -----------------------------------------------------------------------------

def cluster_points(list_of_points, cent_1, cent_2):
    
    cluster_1 = []

    cluster_2 = [] 
    
    for i in range(len(list_of_points)):
    
        if (distance(list_of_points[i], cent_1) < distance(list_of_points[i],
            cent_2)):
            
            cluster_1.append(i)
        
        else:
            cluster_2.append(i)



    return cluster_1, cluster_2


# -----------------------------------------------------------------------------

def get_points(cluster_points_list): 
    
    x_plots = []
    y_plots = []

    for index in range(len(cluster_points_list)): 
        
        
        x_plots.append(cluster_points_list[index][0])
        y_plots.append(cluster_points_list[index][1])

    return x_plots, y_plots

# -----------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Pre-question tasks ----------------------------------------------------------

# Read in the data from the file. ---------------------------------------------

points_df  = pd.read_csv("cs654_exam1_dataset.csv", header=None)


# Visualize the data ---------------------------------------------------------

points_arr = points_df.to_numpy()


X_points = points_df.iloc[ : , 0]
Y_points = points_df.iloc[ : , 1]


plt.ylim([0,105])
plt.xlim([0,105])

plt.scatter(X_points, Y_points)


# Show point for initial cluster --------------------------------------------
#  Assign point [54, 6]
plt.plot(54, 6, 'ro')

# Show point for initial cluster --------------------------------------------
#  Assign point [50, 98]
plt.plot(50, 98, 'go')


plt.show()


# Assign the centroids of 1 and 2 the points ----------------------------------


centroid_1_pt = [54, 6]
centroid_2_pt = [50, 98]


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 7
#
# Use cs654_exam1_dataset.csv and Manhattan distance for question 7 and 
# question 8. Assign point [54, 6] as the initial centroid for Cluster 1, 
# and point [50, 98] as the initial centroid for Cluster 2.
#
# How many points will be assigned to Cluster 1 after the first loop?
# 

cluster1, cluster2 = cluster_points(points_arr, centroid_1_pt, centroid_2_pt)


print("\nQuestion 7: \n\nThe number of points assigned to Cluster 1 is:  ",
      len(cluster1))


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 8
#
# Use cs654_exam1_dataset.csv and Manhattan distance for question 7 and 
# question 8. Assign point [54, 6] as the initial centroid for Cluster 1, and 
# point [50, 98] as the initial centroid for Cluster 2. 
# 
# How many points will be assigned to Cluster 2 after the first loop?
# 

print("\nQuestion 8: \n\nThe number of points assigned to Cluster 2 is:  ",
      len(cluster2))


# Visualize the clusters -----------------------------------------------------

cluster_points_list_cl1 = []
cluster_points_list_cl2 = []


for index in cluster1:
    
    cluster_points_list_cl1.append(points_arr[index])


for index2 in cluster2:
    
    cluster_points_list_cl2.append(points_arr[index2])


x_plots = []
y_plots = []


x_plots, y_plots = get_points(cluster_points_list_cl1)

plt.scatter(x_plots, y_plots, color="pink")

x_plots_2 = []
y_plots_2 = []


x_plots_2, y_plots_2 = get_points(cluster_points_list_cl2)



plt.scatter(x_plots_2, y_plots_2 , color="blue")


#  Assign point [54, 6]
plt.plot(54, 6, 'r+')

plt.plot(50, 98, 'r+')

plt.show()

























