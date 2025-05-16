# -*- coding: utf-8 -*-
"""
Created on Fri May 16 04:27:25 2025

@author: ntcrw


Note: 
    
    - Uses MultinomialNB classifier



"""

import numpy as np
import pandas as pd


from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

all_data_df = pd.read_csv("cs654_module_13_homework_dataset.csv")

positive_200_df = all_data_df.head(200)

negative_200_df = all_data_df.tail(200)


# Generate positive words list -------------------------------------------------
reviews_positive_200 = positive_200_df.iloc[ : ,0 ].to_list() 

# Generate negative words list ------------------------------------------------
reviews_negative_200 = negative_200_df.iloc[ : ,0 ].to_list() 


# Positive reviews words list -------------------------------------------------

reviews_positive_200_words_list = []
reviews_positive_200_words = []

for review in reviews_positive_200:
    
    splitted_words = review.split(", ")
    
    # append to a list of list of the words 
    reviews_positive_200_words_list.append(splitted_words)
    
    # append the splitted words to the list ---------
    for word in splitted_words:
        
        reviews_positive_200_words.append(word)
        

# Negative review words lists -------------------------------------------------

reviews_negative_200_words_list = []
reviews_negative_200_words = []

for review in reviews_negative_200:
    
    splitted_words = review.split(", ")
    
    # append to a list of list of the words 
    reviews_negative_200_words_list.append(splitted_words)
    
    # append the splitted words to the list ---------
    for word in splitted_words:
        
        reviews_negative_200_words.append(word)



# All the distinct words in both lists ---------------------------------------

attribute_words = list( set(reviews_negative_200_words + reviews_positive_200_words))


# -----------------------------------------------------------------------------
# Transform positive reviews into one-hot encoding ----------------------------

positive_vectors = []


for ind in range(len(reviews_positive_200_words_list)):
    
    vector_p = []
    
    for ind2 in range(len(attribute_words)):
        
        if attribute_words[ind2] in reviews_positive_200_words_list[ind]:
            
            vector_p.append(1)
        else:
            
            vector_p.append(0)
            
    positive_vectors.append(vector_p)


# Transform negative reviews into one-hot encoding ----------------------------

negative_vectors = []


for ind in range(len(reviews_negative_200_words_list)):
    
    vector_n = []
    
    for ind2 in range(len(attribute_words)):
        
        if attribute_words[ind2] in reviews_negative_200_words_list[ind]:
            
            vector_n.append(1)
        else:
            
            vector_n.append(0)
            
    negative_vectors.append(vector_n)


#------------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Create class labels ---------------------------------------------------------


positive_negative_labels =[]

for i in range(200):
    positive_negative_labels.append(1)

for i in range(200):
    positive_negative_labels.append(0)


#-----------------------------------------------------------------------------    
# Convert into numpy array ----------------------------------------------------

X = np.array(positive_vectors + negative_vectors) 


#------------------------------------------------------------------------------
# Convert the labels ----------------------------------------------------------

y = np.array(positive_negative_labels)



# Split the data into training and test sets ----------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5,
                                                    random_state = 42)




# Create the model. -----------------------------------------------------------

DT_model = tree.DecisionTreeClassifier(random_state = 42)


DT_model = DT_model.fit(X_train, y_train)



# Using CV = 2 ----------------------------------------------------------------
scores_2 = cross_val_score(DT_model, X, y, cv = 2)

print("\nUsing CV=2: \n")
print("Cross Validation Scores: ", scores_2)
print("Average CV Score: ", scores_2.mean())
print("Number of CV Scores used in Average: ", len(scores_2)) 



# Using CV =5 -----------------------------------------------------------------

scores_5 = cross_val_score(DT_model, X, y, cv = 5)

print("\nUsing CV=5: \n")
print("Cross Validation Scores: ", scores_5)
print("Average CV Score: ", scores_5.mean())
print("Number of CV Scores used in Average: ", len(scores_5))










