# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:22:32 2024

@author: ntcrw

Notes:


"""

import string
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import csv

in_file = open('amazon_reviews.txt', 'r')

amazon_text = []


for line in in_file:
    amazon_text.append(line)
    

append_test = []
for index in range(len(amazon_text)):
    #print(amazon_text[index])
    append_test.append(amazon_text[index])



list_of_sentences = []

# Break into sentences
for item in append_test:
    list_of_sentences.append(sent_tokenize(item))
    
    
    
#print(list_of_sentences[0])
#print(len(list_of_sentences), "\n\n")


# =============================================================================
# Question 1
# Which of the following description is correct?
"""
tokenize_words = []

# Toekenize the sentences.
for index1 in range(0, len(list_of_sentences)):
    #print(list_of_sentences[index1])
    
    for index2 in range(0, len(list_of_sentences[index1])): 
        
        #new_sentence = list_of_sentences[index1][index2]
        new_sentence = list_of_sentences[index1][index2].translate(str.maketrans('','',string.punctuation))
        
        tokenize_words.extend(word_tokenize(new_sentence))
 
print(len(tokenize_words))
"""

# ============================================================================
# Question 2
#
# For each review in the provided dataset, do the following:
#
#    Remove punctuation marks
#
#    Make every word in lower case
#
#    Lemmatize each word
#
#    Put the processed words of each review in one single line and output all
#    lines into a text dataset.
#
# ============================================================================

lem = nltk.WordNetLemmatizer()


final_words = []

for index1 in range(0, len(list_of_sentences)):
    
    # Break into sentences
    list_of_sentences = []
    
    lemma_words_lst = []
  
    list_of_sentences.extend(sent_tokenize(append_test[index1]))
    
    lower_case = []
    
    for sentence in  list_of_sentences:
        
        # Remove the punctuation marks
        sentence = sentence.translate(str.maketrans('','',string.punctuation))
        
        # Convert to lowercase
        sentence = sentence.lower()
        lower_case.append(sentence)
        
        word_tokens = nltk.word_tokenize(sentence)
        
        for word in word_tokens:
            
            # lemmatize the word.
            lemma_word = lem.lemmatize(word)
            
            # Add to lemmatized words_list
            lemma_words_lst.append(lemma_word)
        
    # add to the list
    final_words.append(lemma_words_lst)
        
#print(final_words)


# Write to a file
with open("cs621_module_11_Heino.txt", 'w', newline='') as outfile:
    wr = csv.writer(outfile)
    wr.writerows(final_words)
 

output_list = []
 
for index in range (0, len(final_words)):
    
    word_string = ""
    
    for index2 in range(0, len(final_words[index])):
        
        word_string = word_string + ' ' + final_words[index][index2]
    
    # append to the main list of 
    output_list.append(word_string.lstrip())  
    
# write list to the file
with open('cs621_module_11_Heino.txt', 'w+') as outfile:
    
    for item in output_list:
        outfile.write('%s\n' %item)

outfile.close()

#==============================================================================











    