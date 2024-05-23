# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:33:20 2024

@author: mehei
"""

import string
import pandas as pd
import matplotlib.pyplot as plt

def word_count(sentence):
   
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))

    word_list = sentence.split()
   
    words = []
    word_count = []
    count = 0
   
    for word in word_list:

       if word not in words:
           # add the word to the list
           words.append(word)
           
    print(words)
    # count the words in the string
    for index in range(0, len(words)):
       # count the number of words
       count = word_list.count(words[index])
       word_count.append(count)
       
    return words, word_count
   
def create_a_data_frame(count_list, word_list):
    print("Create data frame")
   
    word_df = pd.DataFrame(list(zip(word_list, count_list)),
               columns =['Word', 'Freq'])
   
    return word_df


#*****************************************************
word_sentence = 'Hello this is a test.  Hello this is also a test Please count the words in this test'

word_list, word_count = word_count(word_sentence)

#print(word_list, word_count)

words_counts_df = create_a_data_frame(word_count, word_list)

# Show dataframe
print(type(words_counts_df))
print(words_counts_df)

bargraph = words_counts_df.plot.bar(x='Word', y='Freq')

print(bargraph)