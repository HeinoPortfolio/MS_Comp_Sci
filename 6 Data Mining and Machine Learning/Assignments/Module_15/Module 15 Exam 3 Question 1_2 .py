# -*- coding: utf-8 -*-
"""
Created on Mon May 19 14:34:23 2025

@author: ntcrw


Notes:
    
    - Dataset 1 and dataset 2 consist of movie reviews and their true 
      labels (1:positive, 0:negative).

    - Will use the following classifier from Hugging Face to predict each 
      movie review's sentiment.


Note: 
    Each prediction contains a label and a score. For instance, 
    {'label': 'POSITIVE', 'score': 0.9995930790901184}

"""

import pandas as pd
import string

#Methods ----------------------------------------------------------------------


# -----------------------------------------------------------------------------

#------------------------------------------------------------------------------
#Pre-question tasks -----------------------------------------------------------
#------------------------------------------------------------------------------

# Read in the data-------------------------------------------------------------

# Read in the data for the positive reviews into a dataframe ------------------

positive_reviews_df = pd.read_csv("movie_reviews_500_positive.csv")

# Read in the data for the negative reviews into a dataframe ------------------ 

negative_reviews_df = pd.read_csv("movie_reviews_500_negative.csv")

#------------------------------------------------------------------------------

#classifier = pipeline('sentiment-analysis', 
#                     model='distilbert-base-uncased-finetuned-sst-2-english')


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------ 
# Question 1
#
# For the longest review of dataset 1 and dataset 2, what is the number of 
# **words** after punctuation removal? 
#

# Create a list of all the reviews --------------------------------------------

list_of_pos_reviews = positive_reviews_df['text'].to_list() 

# add the negative reviews to the list of reviews -----------------------------

list_of_neg_reviews = negative_reviews_df['text'].to_list()


all_reviews_list = list_of_pos_reviews + list_of_neg_reviews

# Iterate over the list of reviews --------------------------------------------

list_of_lengths = []


for review in all_reviews_list:
    
    translator = str.maketrans('', '', string.punctuation)
    
    # Remove punctuation--------------------------------
    clean_text =  review.translate(translator)
    
    list_of_lengths.append(len(clean_text.split()))
    
 
# Show the results -----------------------------------------------------------

print("\n\nQuestion 1: The longest review after punctuation removal is:  ",
      max(list_of_lengths))
   
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------      
#
# Question 2
#
# For the shortest review of dataset 1 and dataset 2, what is the number of 
# words after punctuation removal?
#

print("\n\nQuestion 1: The shortest review after punctuation removal is:  ",
      min(list_of_lengths))




 
      
































































