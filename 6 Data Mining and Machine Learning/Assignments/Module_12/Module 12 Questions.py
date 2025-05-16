# -*- coding: utf-8 -*-
"""
Created on Thu May 15 21:26:20 2025

@author: ntcrw

Perform data cleaning as (Do not mix the order):

    1) remove punctuation first

    2) remove words contained in dataset 3

    3) normalize every word in their lower case
    
    
Note:
    
    - Dataset 1 has the positive reviews


"""

from nltk.tokenize import word_tokenize
from collections import Counter

import pandas as pd
import string

# -----------------------------------------------------------------------------
# Methods ---------------------------------------------------------------------
# -----------------------------------------------------------------------------

def remove_punctuation(reviews_list):
    
    no_punct_list = []
    
    # 1) Remove the punctuation from the reviews -----------------------------

    for rev in reviews_list:
       
       no_punct =  rev.translate(str.maketrans('','', string.punctuation))
       
       no_punct_list.append(no_punct)
       
    return no_punct_list

# -----------------------------------------------------------------------------

def remove_stopwords(no_punct_list, stop_words):
    
    all_words = [] 
    
    # 2) Remove the stopwords that are contained in dataset 3 -----------------
    
    for element in no_punct_list: 
        
        words = word_tokenize(element)
    
        for word in words:
        
            if word not in stop_words:
            
                all_words.append(word)
    
    return all_words 

#-----------------------------------------------------------------------------

def normalize_words(all_words):
    
    final_list = []
    
    
    # 3) Normalize every word in their lower case -----------------------------
    for element in all_words:
    
        final_list.append(element.lower())

    return final_list

#------------------------------------------------------------------------------

def feature_vector(attr_wrds, rev_cleaned):


    feature_vects = []

    for ind in range(0, 2):
        
        feature_vect = []
        
        for wrd in attr_wrds:
            
            if wrd in rev_cleaned[ind]:
                
                feature_vect.append(1)
                
            else:
            
                feature_vect.append(0)

        feature_vects.append(feature_vect)
        
    return feature_vects

#------------------------------------------------------------------------------    

# Pre-question tasks ----------------------------------------------------------
#------------------------------------------------------------------------------


# Read the data into a dataframe.---------------------------------------------

dataset_1_df = pd.read_csv("cs654_module_12_dataset1.csv")
dataset_2_df = pd.read_csv("cs654_module_12_dataset2.csv")

stop_words_df = pd.read_csv("cs654_module_12_dataset3.csv", header=None)


#------------------------------------------------------------------------------    
#------------------------------------------------------------------------------
#
# Question 1
#
# What is the number of words in dataset 1 after data cleaning? 


# 1) Remove the punctuation from the reviews ----------------------------------

reviews = dataset_1_df['text'].to_list()

no_punctuation = remove_punctuation(reviews)


# 2) Remove the stopwords that are contained in dataset 3 ---------------------

stop_words_list = stop_words_df.iloc[:, 0].to_list()

no_stopwords = remove_stopwords(no_punctuation, stop_words_list)



# 3) Normalize every word in their lower case ---------------------------------

final_list_ds1 =normalize_words(no_stopwords)


print("\nQuestion 1: \nThe number of words in dataset (1) after cleaning is: ", 
      len(final_list_ds1))

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 2
#
# What is the number of words in dataset 2 after data cleaning?
#
 
 
# 1) Remove the punctuation from the reviews ----------------------------------

reviews2 = dataset_2_df['text'].to_list()
no_punctuation2 = remove_punctuation(reviews2)


# 2) Remove the stopwords that are contained in dataset 3 ---------------------


no_stopwords2 = remove_stopwords(no_punctuation2, stop_words_list)


# 3) Normalize every word in their lower case ---------------------------------

final_list_ds2 =normalize_words(no_stopwords2)


print("\nQuestion 2: \nThe number of words in dataset (2) after cleaning is: ", 
      len(final_list_ds2))


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 3
#
# What is the number of common distinct words in dataset 1 and dataset 2
#

# Use set() to create a set with only unique words 

#print("Dataset 1 final list size: ", len(final_list_ds1))
#print("Dataset 2 final list size: ", len(final_list_ds2))


# Create the set using the final sets of cleaned data -------------------------


print("\nQuestion 3: ")

common_words = list(set((final_list_ds1 + final_list_ds2)))
print("\nNumber of words common in dataset 1 and dataset 2 is: \t",
       len(common_words))


in_both_reviews = set(final_list_ds1).intersection(set(final_list_ds2))
print("\nNumber of words in dataset 1 and dataset 2 is: \t", 
      len(in_both_reviews))


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 4
#
# What is the size of one-hot-encoding attributes/features?
#

# Create attribute words list -------------------------------------------------

attribute_words = list(set(final_list_ds1 + final_list_ds2))

reviews_cleaned = [final_list_ds1, final_list_ds2]


feature_vectors = feature_vector(attribute_words , reviews_cleaned)

print("\nQuestions 4: \n\nFeature vector: ", len(feature_vectors[0]))


# -----------------------------------------------------------------------------
#
# Question 5 
#
# What is the highest word frequency? 
#

combined_word_list = final_list_ds1 + final_list_ds2

# Using the 'collections' module ----------------------------------------------
highest_word_freq = Counter(combined_word_list).most_common(5)

print("\nQuestion 5: \n\nThe word with the highest frequency is: ", 
      highest_word_freq[0][1])


# -----------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 6
#
# Using one-hot-encoding, how many 1s are there in the first positive review? 


# Get the first postive review from the first dataset ------------------------

first_pos = dataset_1_df.iloc[0,0]

first_pos_no_punc = first_pos.translate(str.maketrans('','',
                                                      string.punctuation))

 
all_words6 = []
   
words = word_tokenize(first_pos_no_punc) 

for wrd in words:
    
    if wrd not in stop_words_list:
        
        all_words6.append(wrd.lower())
        
        
# using the attributes created earlier --------------------------------------
# Create a vector for the review ---------------------------------------------

feature_vect_q6 = []

for attr in attribute_words:
   
   if attr in all_words6:
       
       feature_vect_q6.append(1)
   else:
       
       feature_vect_q6.append(0)
         
one_freq = Counter(feature_vect_q6).most_common(2)

print("\nQuestion 6:\n \nFrequency of 1s in the first review: ", one_freq)
 








  
  
       
    
  