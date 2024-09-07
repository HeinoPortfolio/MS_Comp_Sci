# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:19:50 2024

@author: ntcrw

Notes:
    1) Uses the module_11_results file for the input file
    2) Runtime can take about ?? minutes.
    3) Number of distinct words:     51,975
    4) 
    
"""

from wordcloud import  WordCloud
import matplotlib.pyplot as plt
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag

# =============================================================================
# Pre-question tasks

infile = open('module_11_results.txt')


# Load the data into a list
raw_text_list = []

infile.seek(0)

for line in infile:
    
    raw_text_list.append(line)


infile.close()

print("\n\n Read in the file!! \n\n")
# =============================================================================

# =============================================================================
# Question 3
# Apply POS Tagging on the dataset and only keep words tagged with NN and NNP.
# Create one more wordcloud. 
# Name this image as wordcloud 3 and submit it. The wordcloud should 
# contain NN and NNP only.
#
#
# Note: this could have been done with a single list.  Using two lists was to 
# aid maiking sure the the nnp words were being extacted properly.
# 
# =============================================================================

pos_tags = []
pos_nn = []
pos_nnp = []
both_nnp_nn_list = []

for sentence in raw_text_list:
    
    pos = pos_tag(word_tokenize(sentence))
    
    for index in range(0, len(pos)):
        
        if  pos[index][1] == 'NN':
            
            # add to the list of NN words
            pos_nn.append(pos[index][0])
            
        elif pos[index][1] == 'NNP':
            #print("NNP\n")
            pos_nnp.append(pos[index][0])

print("\n\nCreated the NN and NNP list!!! \n\n")            
            
# Join the two lists
both_nnp_nn_list = pos_nn + pos_nnp 


# Create file with all NN and NNP words
# to view the list of words

"""
with open('all_nn_nnp.txt', 'w') as f:
    
    for line in both_nnp_nn_list:
        f.write(f"{line}\n")

"""

# Print status
print("Joined lists!!!! \n")

 
# Generate a list of distinct words
distinct_words = list(set(both_nnp_nn_list))

#print("\n Generated distinct words list!!! \n")


# to view the list of words
with open('all_distinct.txt', 'w') as f:
    for line in distinct_words:
        f.write(f"{line}\n")



# Create a word count dictionary
word_freq_dict = {}

for word in distinct_words:
    word_freq_dict[word] = 0
    
#print("\n\n Created word count dictionary!!\n")


print("\n\nStarted compute frequency!!!! \n")
# Compute the frequency of the word.
#for index in range(0, 10000): 
for index in range(0, len(distinct_words)):
    
    key_word = distinct_words[index]
    
    if index % 500 == 0:
        print("Key word: ", key_word, "  Index: ", index)
    
    count = 0
    
    for word in both_nnp_nn_list:
        
        if word == key_word:
            count += 1
    
    word_freq_dict[key_word] = count        

print("\nEnded Word frequency!!! \n\n")


# Create the word cloud
wordcloud4 = WordCloud(max_font_size=200, stopwords=None, max_words=20
                       , background_color='White').generate_from_frequencies(word_freq_dict)


# Show the cloud as an image
plt.tick_params(top=False, bottom=False, left=False, right=False
                , labelleft=False, labelbottom=False)

plt.imshow(wordcloud4)


# ============================================================================= 
            
    
    
    
    
    
    
    
        
        
    
    
