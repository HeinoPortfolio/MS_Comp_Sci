# -*- coding: utf-8 -*-
"""
Created on Thu May 15 21:02:33 2025

@author: ntcrw


- Each row represents a movie review. The words column contains the words left
  **after** cleaning.

- The label column indicates its sentiment: 1 is positive and 0 is negative. 


"""


import pandas as pd 


from sklearn.naive_bayes import MultinomialNB




# Pre-question tasks ----------------------------------------------------------

dataset_df  = pd.read_csv("cs654_module_13_homework_dataset.csv")


postive_df = dataset_df[dataset_df['label'] == 1]

negative_df = dataset_df[dataset_df['label'] == 0].reset_index(drop=True)

 

# Create lists of lists of positive words  andnegative words ------------------
postive_words  = postive_df['words'].to_list()

negative_words = negative_df['words'].to_list()


all_pos_words = []
all_neg_words = []

# Extract all the positive words ----------------------------------------------

for item in postive_words:
    
    splitted_word_1 = item.split(", ")
    
    for word in splitted_word_1:
        
        all_pos_words.append(word)


for item in negative_words:
    
    splitted_word_2 = item.split(", ")
    
    for word in splitted_word_2:
        
        all_neg_words.append(word)    
    
#------------------------------------------------------------------------------

# Create a feature / attribute list--------------------------------------------
# Use a unique set of words that contain words from both the positive and 
# negative reviews.
    
attribute_words = list(set(all_pos_words + all_neg_words))







































