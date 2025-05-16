# -*- coding: utf-8 -*-
"""
Created on Thu May 15 18:24:42 2025

@author: ntcrw


Datasets used:

- cs654_module_12_dataset1.csv   (positive reviews) -->     Dataset 1
- cs654_module_12_dataset2.csv   (negative reviews) -->     Dataset 2
- cs654_module_12_dataset3.csv   (stopwords)        -->     Dataset 3    

Perform data cleaning as (Do not mix the order)

   - 1) remove punctuation first

   - 2) remove words contained in dataset 3

   - 3) normalize every word in their lower case


"""

from nltk.tokenize import sent_tokenize, word_tokenize

import csv
import pandas as pd
import string


# Pre-question tasks ----------------------------------------------------------

# Read the data into a dataframe.

dataset_1_df = pd.read_csv("cs654_module_12_dataset2.csv")

stop_words_df = pd.read_csv("cs654_module_12_dataset3.csv", header=None)

stop_words = stop_words_df.iloc[:, 0].to_list()



list_of_reviews = []


# iterate over the dataframe of reviews ---------------------------------------
for ind in range(0, len(dataset_1_df)):
    
    review  = dataset_1_df.iloc[ind, 0]
    
    # Break Review into a list of sentences------
    
    list_of_reviews.append(sent_tokenize(review))


# Break into sentences --------------------------------------------------------

list_of_sentences = []

for review in list_of_reviews:
    
    
    for index1 in range(0, len(review)):
        
        list_of_sentences.append(review[index1])


# 1) Remove punctuation from the sentences ------------------------------------

sent_no_punct = []

for sentence in list_of_sentences:
    
    no_punct = sentence.translate(str.maketrans('','',
                                     string.punctuation))

    sent_no_punct.append(no_punct)


# 2) Remove the stopwords from the sentence -----------------------------------

cleaned_words = []

for no_punct_sent in sent_no_punct:
    
    # Tokenize each sentence in the list --------------
    
    word_tokens = word_tokenize(no_punct_sent)
    
    for wrd in word_tokens:
        
        if wrd not in stop_words: 
            
            cleaned_words.append(wrd)

# 3) Normalize the words to their lowercase -----------------------------------

final_list = []

for wrd in cleaned_words:
    
    final_list.append(wrd.lower())


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 2
#
# What is the number of words in dataset 2 after data cleaning?
#

print("Question 1: \nThe number of words in dataset 1 is: ", len(final_list))


with open('ds2_cleaned.csv', 'w', newline='') as file:
    
    writer = csv.writer(file)
    writer.writerow(final_list)