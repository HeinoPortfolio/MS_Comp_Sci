# -*- coding: utf-8 -*-
"""
Created on Tue May 21 04:25:43 2024

@author: mehei
"""

from textblob import TextBlob
import re # regular expressions
import nltk

def show_menu():
    ''' show the menu options, and return a choice as a string, if valid.
        Otherwise, loop to prompt the user to make another choice. '''
    while True:
        print('Please make a choice:')
        print('1. Enter a new corpus of text.')
        print('2. Print a report summarizing the total number of words and sentences.')
        print('3. Print a list of all the noun phrases.')
        print('4. Print a sentiment analysis.')
        print('5. Exit the program.')
        choice = input()
        # process choice, using a regular expression to see if they entered a valid choice
        if re.fullmatch(r'^[1-5]$', choice):  # if valid
            return choice
        else:
            print('That is not a valid choice.  Please enter a number.')
            
#*****************************************************************************

def read_file(filename):
    ''' Open a file, and convert the contents to a TextBlob, then return it.
        The filename is passed to the function as an argument.'''
    try:
        datafile = open(filename, 'r')
        # read all lines into a list and close file
        text_lines = datafile.readlines()
        datafile.close()
        # combine the list into a single string, with spaces between items
        text_string = ' '.join(text_lines)
        # convert to a TextBlob
        return TextBlob(text_string)
    except FileNotFoundError:  
        # if there was no file by that name, return an error
        contents = f'There is no file named {filename} in this directory.'
        return TextBlob(contents)
    #Remember to remove the return error statement 

#******************************************************************************

def generate_counts(text):
    
    ''' Calculates the number of words in the text and the number
        sentences '''
        

    output_str =''
    
    #number of words
    number_of_words = len(text.words)
    
    # number of sentences
    number_of_sentences = len(text.sentences)
    
    output_str = "The total number of words is "+ str(number_of_words) + "\n"
    
    output_str2 = "The total number of sentences is " + str(number_of_sentences)
    
    return output_str + output_str2

#*****************************************************************************

def generate_np(text):

    
    noun_phrase_list = ''
   
    for noun_phrase in text.noun_phrases:

        # iterate through the list
        noun_phrase_list += noun_phrase + '\n'
           
    return noun_phrase_list
    

#******************************************************************************

def generate_sentiment(text):
    
    #print("Senitment")
  
    
    pol_str = "The overall sentiment polarity of this selection is "
    obj_str = "The overall sentiment objectivity is "
    
    
    results_str = pol_str + str(text.sentiment.polarity) +'\n' + obj_str + str(text.sentiment.subjectivity)
    
    return results_str
  
    




#*****************************************************************************





# test the function 
filename = 'data_science.txt'
filename2 = 'computer_science.txt'
textblob = read_file(filename)

#print(len(textblob.words))
#generate_np(textblob)
#str_counts = generate_counts(textblob)

#print(str_counts)

#str_np = generate_np(textblob)

#print(str_np)

sent_str = generate_sentiment(textblob)

print(sent_str)





















