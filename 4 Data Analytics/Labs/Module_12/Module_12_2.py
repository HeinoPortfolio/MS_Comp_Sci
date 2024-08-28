# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:32:55 2024

@author: ntcrw
"""
from wordcloud import  WordCloud
import matplotlib.pyplot as plt
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag


data_raw =[]

fl = open("module_11_results.txt")

fl.seek(0)

for line in fl:
    
    data_raw.append(line)

fl.close()


pos_tags_lst = []

for index in range(1, len(data_raw)):
    
    review = data_raw[index]
    
    # break into sentences
    sentences = sent_tokenize(review)

    
    for sentence in sentences:
         
        sentence.strip()
        sentence = sentence.translate(str.maketrans('','',string.punctuation))
        
        pos = pos_tag(word_tokenize(sentence))
        
       
        for index in range(0, len(pos)):
        
            
            if (pos[index][1] == 'NN') or (pos[index][1] == 'NNP'):
                
                # add to the list
                pos_tags_lst.append(pos[index])
