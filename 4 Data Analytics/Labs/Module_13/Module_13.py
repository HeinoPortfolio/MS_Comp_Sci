# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:47:11 2024

@author: ntcrw

Notes:
    1) Number of postive words:         2006
    2) Number of negative words:        4782
    3) Number of reviews:               25486
    4) Time to run 4:00 minutes
    5) Number of positive reviews       18761  
    6) Number of negative reviews       4301
    7) Number of neutral reviews        2424
    
"""
import string
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import csv

# Read in the positive and negative word lists
pos_words_list = []
neg_words_list = []


positive_reviews = 0
negative_reviews = 0
neutral_reviews = 0

# Read the positive words list.
in_file = open('positive_words_list.txt')

in_file.seek(0)

for line in in_file:
    
    pos_word = line.strip()
    pos_words_list.append(pos_word)

in_file.close()

# *****************************************************************************

in_file2 = open('negative_words_list.txt')

in_file2.seek(0)

for line in in_file2:
    
    neg_word = line.strip()
    neg_words_list.append(neg_word)

in_file2.close()

#print(neg_words_list)



# Read in the Amazon reviews
in_file3 = open('amazon_reviews.txt', 'r')

amazon_reviews = []


for line in in_file3:
    amazon_reviews.append(line)

in_file3.close()

"""
# Create a dictionary the will hold the sentiment of the review.
dictionary_keys =[]
for dict_index in range(0, 10): #len(amazon_reviews)):
    
    dictionary_keys.append("Review " + str(dict_index + 1)) 
    
# Create the dictionary
sentiment_dict = dict.fromkeys(dictionary_keys)  
"""

# =============================================================================
# Question 1
# Which one of the following descriptions is correct?
# =============================================================================

#print("Number of negative words: ", len(neg_words_list))
#print("Number of positive words: ", len(pos_words_list))

# =============================================================================

# =============================================================================
# Question 2
# A positive review is defined as the number of matched positive words is more 
# than the number of matched negative words.
#
# Which one of the following descriptions is correct?
# =============================================================================

"""
for review_index in range(0, len(amazon_reviews)):
    
    review = amazon_reviews[review_index]
    
    number_of_positive = 0
    number_of_negative = 0
    
    # break into sentences.
    sentences = sent_tokenize(review)
    
    for sentence_index in range(0, len(sentences)):
        
        sentences[sentence_index] = sentences[sentence_index].translate(str.maketrans('','',string.punctuation))
            
    for sentence in sentences:
        
        # split the sentence into its words.
        review_words = sentence.split()
       
        for word in review_words:
            
            word = word.lower()
         
            # Check to see if the word is postive or negative
            if word in pos_words_list:
                
                # Increment the positive count
                number_of_positive += 1
                
            if word in neg_words_list:
                
                number_of_negative += 1
                
        
    #print("Number of positive words", number_of_positive)  
    #print("Number of negative words", number_of_negative) 
    

    # See if the review was postive or negative.
    if number_of_positive > number_of_negative:
        
        # assign the score to the review dictionary
        key = "Review " + str(review_index + 1)
        sentiment_dict[key] = 'Positive'
        
    elif(number_of_positive < number_of_negative):
       
        key = "Review " + str(review_index + 1)
        sentiment_dict[key] = 'Negative'
        
    else:
        
        key = "Review " + str(review_index + 1)
        sentiment_dict[key] = 'Neutral'
    

# Count the number of positive reviews
for key in sentiment_dict.keys():
    
    if sentiment_dict[key] =='Negative':
        
        negative_reviews += 1
        
    elif sentiment_dict[key] =='Positive':
        
        positive_reviews += 1
        
    elif sentiment_dict[key] =='Neutral':
       
        neutral_reviews += 1
        
    else:
        print("Error!")


print("\nPositive reviews: ", positive_reviews)

"""

#===========================================================================
# Question 3
# A negative review is defined as the number of matched positive words is less 
# than the number of matched negative words.
#
# Which one of the following descriptions is correct? 
# ============================================================================

#print("\nNegative reviews: ", negative_reviews)


#=============================================================================
# Question 4
# A neutral review is defined has equal number of matched positive and negative 
# words, or has no word matched to positive and negative word lists. 
#
# Which one of the following descriptions is correct?
# =============================================================================

#print("\nNeutral reviews: ", neutral_reviews)


# For testing only.
#print("Distinct values in dictinary: ", list(set(sentiment_dict.values())))

# =============================================================================

# Questions 5 and 6 ===========================================================
#==============================================================================
# Question 5
# 
# Which one of the following positive words is less matched than the other 
# three positive words?
# =============================================================================
"""
like_count = 0
great_count = 0
good_count = 0
wonderful_count = 0

for review_index in range(0, len(amazon_reviews)):

    review = amazon_reviews[review_index]

    # break into sentences.
    sentences = sent_tokenize(review)
 
    for sentence_index in range(0, len(sentences)):
     
        sentences[sentence_index] = sentences[sentence_index].translate(str.maketrans('','',string.punctuation))

    for sentence in sentences:
     
         # split the sentence into its words.
         review_words = sentence.split()
    
         for word in review_words:
         
             word = word.lower()
      
             # Check to see if the word is positive or negative
             if word == 'like':
                 
                 #print("\n like")
                 # increment the count
                 like_count += 1
                 
             elif word == 'great':
                 
                 #print('\n great')
                 # increment the count
                 great_count += 1
                 
             elif word == 'good':
                 
                 #print('\n good')
                 # increment the count
                 good_count += 1    
                 
             elif word == 'wonderful':
             
                 #print('\n wonderful')
                 wonderful_count += 1
             
             
# show the results          
print("Number of like words", like_count)  
print("Number of great words", great_count) 
print("Number of good words", good_count)
print("Number of wonderful words", wonderful_count)
"""

# =============================================================================
# Question 6
# 
# Which one of the following negative words is less matched than the other 
# three negative words?
# =============================================================================

bad_count = 0
hard_count = 0
plot_count = 0
slow_count = 0

for review_index in range(0, len(amazon_reviews)):

    review = amazon_reviews[review_index]
    
    # break into sentences.
    sentences = sent_tokenize(review)
    
    for sentence_index in range(0, len(sentences)):
     
        sentences[sentence_index] = sentences[sentence_index].translate(str.maketrans('','',string.punctuation))
        
        #print(sentences[sentence_index])
        for sentence in sentences:
 
            # split the sentence into its words.
            review_words = sentence.split()

            for word in review_words:
     
                word = word.lower()
  
                # Check to see if the word is positive or negative
                if word == 'bad':
             
                    #print("\n bad")
                    # increment the count
                    bad_count += 1
             
                elif word == 'hard':
             
                    #print('\n hard')
                    # increment the count
                    hard_count += 1
             
                elif word == 'plot':
             
                    #print('\n plot')
                    # increment the count
                    plot_count += 1    
             
                elif word == 'slow':
         
                    #print('\n slow')
                    slow_count += 1


# show the results          
print("Number of bad words: ", bad_count)  
print("Number of hard words: ", hard_count) 
print("Number of plot words: ", plot_count)
print("Number of slow words: ", slow_count)











