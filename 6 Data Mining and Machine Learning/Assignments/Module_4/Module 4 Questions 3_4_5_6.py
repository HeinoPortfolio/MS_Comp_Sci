# -*- coding: utf-8 -*-
"""
Created on Tue May 13 23:03:00 2025

@author: ntcrw
"""

import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
import seaborn as sns

from sklearn.cluster import KMeans


warnings.filterwarnings('ignore')


# Methods --------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


# Read in the dataset ---------------------------------------------------------

points_df = pd.read_csv("homework_4_dataset.csv")

# convert the dataframe into a list -------------------------------------------

points_list = points_df.values.tolist()

#print(points_list)

# convert list into np array --------------------------------------------------

pts = np.array(points_list)


# print(pts)

# Visualize the points of the dataset ----------------------------------------
sns.scatterplot(
    
    x='X',
    y='Y',
    data=points_df
    
    )

plt.show()

# End visual ------------------------------------------------------------------

# -----------------------------------------------------------------------------
#
# Question 3
#
# Using the scikit-learn KMeans API and set k = 2, 
# what is the final SSE value? 

# Create two cluster of the data

kmeans2 = KMeans(n_clusters=2, random_state=77).fit(pts)

# save the cluster labels
cluster_labels = list(kmeans2.labels_)

# append the labels to the dataframe
points_df['Labels_2'] = cluster_labels

# Create a plot using seaborn

sns.scatterplot(
    
    x='X',
    y='Y',
    data=points_df,
    hue='Labels_2'
    
    )

# add centroids to the scatter plot

centroid_1 = kmeans2.cluster_centers_[0]
centroid_2 = kmeans2.cluster_centers_[1]

plt.scatter(centroid_1[0],centroid_1[1] , color='r')
plt.scatter(centroid_2[0],centroid_2[1] , color='g')

plt.show()


# Show the SSE or the inertia ------------------------------------------------
sse = kmeans2.inertia_

print("\nQuestion 3: \nThe SSE or inertia with two groups: ", sse)

# ----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 4
#
# Using the sckikt-learn KMeans API, set k = 3, 
# what is the final SSE value?


kmeans3 = KMeans(n_clusters=3, random_state=77).fit(pts)


# save the cluster labels
cluster_labels3 = list(kmeans3.labels_)

# append the labels to the dataframe
points_df['Labels_3'] = cluster_labels3

# Create a plot using seaborn

sns.scatterplot(
    
    x='X',
    y='Y',
    data=points_df,
    hue='Labels_3'
    
    )

# add centroids to the scatter plot

centroid_1 = kmeans3.cluster_centers_[0]
centroid_2 = kmeans3.cluster_centers_[1]
centroid_3 = kmeans3.cluster_centers_[2]

plt.scatter(centroid_1[0],centroid_1[1] , color='r')
plt.scatter(centroid_2[0],centroid_2[1] , color='g')
plt.scatter(centroid_2[0],centroid_2[1] , color='b')

plt.show()


sse = kmeans3.inertia_

print("\nQuestion 4: \nThe SSE or inertia with three groups: ", sse)

#-----------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 5
#
# Using the scikit-learn KMeans API with k = 2, two clusters will be generated.
# Which one of the following descriptions is correct? 
#

# number in eahc cluster

num_in_cluster2 = points_df['Labels_2'].value_counts()


print("\nQuestion 5: \n")
print("Number of elements in cluster 1: ", num_in_cluster2[0])
print("Number of elements in cluster 2: ", num_in_cluster2[1])


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 6
#
# Using the scikit-learn KMeans API with k = 3, three clusters will be 
# generated. Which one of the following descriptions is correct?
#

num_in_cluster3 = points_df['Labels_3'].value_counts()

print("\n\nQuestion 6: \n")
print("Number of elements in cluster 1: ", num_in_cluster3[0])
print("Number of elements in cluster 2: ", num_in_cluster3[1])
print("Number of elements in cluster 3: ", num_in_cluster3[2])
















