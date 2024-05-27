# -*- coding: utf-8 -*-
"""
Created on Mon May 27 00:46:13 2024

@author: mehei
"""

import requests, inspect
from bs4 import BeautifulSoup
from textblob import TextBlob
from textatistic import Textatistic


def extract_text(addr):
   ''' visit the website in the address, extract the text using Beautiful Soup,
        remove the html tags and return the text'''
   
   r = requests.get(addr) 
   
   soup = BeautifulSoup(r.content, 'html.parser')
   
   
   # Remove the HTML tags from the returned webpage.
   content_text = soup.get_text(strip=True)
   
   
   return content_text


def print_sentences(text, num_sentences):
    ''' print the first few sentences in the text, where the number of sentences
        is given by num_sentences '''
    
    
    content_str = ""
    content_list = []
    
    # Create a text blob from the HTml content
    content_blob = TextBlob(text)
    
    
    content_list = list(content_blob.sentences)
    
    for index in range(0, num_sentences):
        content_str = content_str+'Sentence #'+str(index)+': '+ str(content_list[index])
        
    print(content_str)
    
    
# *****************************************************************************

def readability(text):
    ''' return the readability score reported by Textastistic for Dale-Chall '''
    
    
    readability_score = 0.0
    
    readability = Textatistic(text)
    
    readability_score = readability.dalechall_score
    
    
    return readability_score
   
# *****************************************************************************

def sentiment(text):
    ''' return the sentiment score reported by TextBlob '''
   
    
    # create a textblob from text
    textblob = TextBlob(text)
    
    # return the sentiment for the text.
    
    return textblob.sentiment.polarity
    
    
# *****************************************************************************
    
    
# Test Functions start here. ##################################################
##############################################################################

# Try out your extract_text function*******************************************


#addr = "https://www.cbsnews.com/news/ketanji-brown-jackson-supreme-court-senate-confirmation-first-black-woman/"
#text = extract_text(addr)
#print(text)

# test print_sentences function ***********************************************
#num_sentences = 1
#print_sentences(text, num_sentences)


# Test readability function ***************************************************
#addr = "https://www.cbsnews.com/news/ketanji-brown-jackson-supreme-court-senate-confirmation-first-black-woman/"
#text = extract_text(addr)
#print(readability(text))

addr = "https://www.cbsnews.com/news/ketanji-brown-jackson-supreme-court-senate-confirmation-first-black-woman/"
text = extract_text(addr)
print(sentiment(text))


























