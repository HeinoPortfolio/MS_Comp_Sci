# -*- coding: utf-8 -*-
"""
Created on Wed May 22 02:28:07 2024

@author: mehei
"""

import nltk
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def num_sentences(text):
    ''' Determine the number of sentences in the text '''
    
    # Create a textblob 
    text_blob = TextBlob(text)
    
    # Count the sentences. 
    sentence_number = len(text_blob.sentences)
    
    return sentence_number
    
#******************************************************************************

def report_sentiment(text):
    '''report the sentiment using emoji'''
    

    grinning_face = 0x1F600
    slight_smiling_face = 0x1F642 	
    neutral_face = 0x1F610
    slight_frown_face = 0x1F641
    frowning_face = 0x1F61f
    
    polarity_str = 'Polarity: '
    
    # Create a textblob 
    text_blob = TextBlob(text)
    
    
    if text_blob.sentiment.polarity > 0.6:
        polarity_str = polarity_str + str(text_blob.sentiment.polarity) + f' {grinning_face:c}'
    elif text_blob.sentiment.polarity > 0.35:
        polarity_str = polarity_str + str(text_blob.sentiment.polarity) + f' {slight_smiling_face:c}'
    elif text_blob.sentiment.polarity > -0.35:
        polarity_str = polarity_str + str(text_blob.sentiment.polarity) + f' {neutral_face:c}'
    elif text_blob.sentiment.polarity > -0.6:
        polarity_str = polarity_str + str(text_blob.sentiment.polarity) + f' {slight_frown_face:c}'
    else:
        polarity_str = polarity_str + str(text_blob.sentiment.polarity) + f' {frowning_face:c}' 
    
    return polarity_str


#******************************************************************************
def report_NBA_sentiment(text):
    '''return a string reporting the TextBlob Naive Bayes sentiment 
    , and emoji '''


    frowning_face = 0x1F61f
    grinning_face = 0x1F600
    
    polarity_str = 'Polarity:'
    
    # Create a textblob 
    text_blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

    #print(type(text_blob.sentiment[0]))
    if text_blob.sentiment[0] == 'neg':
        polarity_str = polarity_str + f' {frowning_face:c} ' + 'negative' 
    else:
        polarity_str = polarity_str + f' {grinning_face:c} ' + 'positive'
    
    return polarity_str





#******************************************************************************


"""
test_text = 'This is sentence one. This is sentence two. There should be three sentences'
text1 = 'Today is a lousy day.'
text2 = 'Textblob is amazingly simple to use. What great fun!'
text3 = 'Today was an amazing day! Hopefully, tomorrow will also be great.'
"""


test1 = 'Today is a great day!'
test2 = 'Today is an ok day.'
test3 = 'Today is a day'
test4 = 'Today is a lousy day.'
test5 = 'Today was a terrible day.'


text1 = 'Today is a lousy day.'
text2 = 'Textblob is amazingly simple to use. What great fun!'




#print(num_sentences(test_text))
print(report_sentiment(test5))
print(report_NBA_sentiment(test5))














