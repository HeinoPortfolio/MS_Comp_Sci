# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:02:00 2024

@author: ntcrw
"""

from wordcloud import  WordCloud
import matplotlib.pyplot as plt
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag

text = open('module_11_results.txt').read()
"""
#==============================================================================
# Question 1
# Create a wordcloud out of the dataset created from module 11.
# Name this image as wordcloud 1 and submit it. This wordcloud 
# should contain stop words like 'the'.

text_words =  text.split(" ")
distinct_words = list(set(text_words))


word_freq_dict = {key: 0 for  key in distinct_words}


for word in text_words:
        
        # increment the count
        word_freq_dict[word] = word_freq_dict[word] + 1


# Generate the WordCloud from frequencies.
new_word_cloud = WordCloud(background_color='white').generate_from_frequencies(word_freq_dict)

# Show the cloud as an image
plt.tick_params(top=False, bottom=False, left=False, right=False
                , labelleft=False, labelbottom=False)

plt.imshow(new_word_cloud)

# Write image to a file.
new_word_cloud.to_file('wordcloud 1.png')

# =============================================================================        


# =============================================================================
# Question 2        
# Remove the stop words first, then create another wordcloud. 
# Name this image as wordcloud 2 and submit it. This wordcloud 
# should contain adjective words like 'great'.


stop_words_wc = WordCloud(width=600, height=600,background_color='yellow').generate(text)

# Show the cloud as an image
plt.tick_params(top=False, bottom=False, left=False, right=False
                , labelleft=False, labelbottom=False)

plt.imshow(stop_words_wc)

# write image to a file
stop_words_wc.to_file('wordcloud 2.png')
# =============================================================================
"""

# =============================================================================
# Question 3
# Apply POS Tagging on the dataset and only keep words tagged with NN and NNP.
# Create one more wordcloud. 
# Name this image as wordcloud 3 and submit it. The wordcloud should 
# contain NN and NNP only.

pos_tags_lst = []


# read the original file

f = open("amazon_reviews.txt")

# Load the data into a list
amazon_data_raw =[]

f.seek(0)

for line in f:
    
    amazon_data_raw.append(line)

f.close()

for index in range(0, len(amazon_data_raw)):
    
    review = amazon_data_raw[index]
    
    # break into sentences
    sentences = sent_tokenize(review)

    
    for sentence in sentences:
         
        sentence.strip()
        sentence = sentence.translate(str.maketrans('','',string.punctuation))
        
        pos = pos_tag(word_tokenize(sentence))
        
       
        for index in range(0, len(pos)):
        
            
            if (pos[index][1] == 'NN') or (pos[index][1] == 'NNP'):
                
                # add to the list
                pos_tags_lst.append(pos[index][0])

        
distinct_words_2 = list(set(pos_tags_lst))

word_freq_dict_2 = {key: 0 for  key in distinct_words_2}



for word in pos_tags_lst:
        
        # increment the count
        word_freq_dict_2[word] = word_freq_dict_2[word] + 1



"""
# get the parts of speech (POS) tags.
pos = pos_tag(word_tokenize(text))

print(pos)

"""

# Generate the WordCloud from frequencies.
word_cloud_3 = WordCloud(background_color='white').generate_from_frequencies(word_freq_dict_2)

# Show the cloud as an image
plt.tick_params(top=False, bottom=False, left=False, right=False
                , labelleft=False, labelbottom=False)

plt.imshow(word_cloud_3)

# Write image to a file.
word_cloud_3.to_file('wordcloud 3.png')


# =============================================================================













