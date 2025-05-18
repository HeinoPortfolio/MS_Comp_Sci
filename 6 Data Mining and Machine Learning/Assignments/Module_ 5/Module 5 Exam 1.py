# -*- coding: utf-8 -*-
"""
Created on Sat May 17 23:52:51 2025

@author: ntcrw
"""

import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd 

from sklearn.metrics.pairwise import euclidean_distances


# Read in the dataset ---------------------------------------------------------

points_df  = pd.read_csv("cs654_exam1_dataset.csv", header=None)

target_pt  = [50, 50]


points_arr = points_df.to_numpy()


X_points = points_df.iloc[ : , 0]
Y_points = points_df.iloc[ : , 1]


plt.ylim([0,105])
plt.xlim([0,105])

plt.scatter(X_points, Y_points)

# Add a point at (2.5, 2.5) with a red circle marker --------------------------
plt.plot(target_pt[0]  , target_pt[1] , 'ro')

plt.show()


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 3
#
#
# Using cs654_exam1_dataset.csv and Euclidean distance, which 
# point(20 points: from point 0 or point 19)has the shortest distance to 
# point (50, 50)?
#

dist_list = []


dist_list = euclidean_distances(points_arr, [[50, 50]])

# Create a dataframe with th distances ---------------------------------------

points_df['Distances'] = dist_list

































