# -*- coding: utf-8 -*-
"""
Created on Sun May 19 23:54:05 2024

@author: mehei
"""
import requests
import matplotlib.pyplot as plot
from wordcloud import WordCloud



def load_localfile():
    
    ''' prompt user for filename, load data into list of lines, return list '''
    
    filename =  input("Enter the file name: ")
    line_list = []
    
    # try to open the file
    while True:
        
        try:
        
            with open(filename, 'r') as datafile:
                line_list = datafile.readlines()
            
            return line_list
    
        except FileNotFoundError:
            print("File not found!")
            filename =  input("Enter the file name: ")
        


def menu():
    
    ''' Menu of the program '''

    print('Please choose an option from the list below.')
    print('1. Analyze a local, user-specified file ')
    print('2. Connect to Project Gutenberg and analyze the U.S. Constitution')
    print('3. Connect to Project Gutenberg and analyze the State of the Union' 
          + 'Addresses for Abraham Lincoln')
    print('4. Quit the progra.')
    
    
    
    option = int(input("Please select an option: "))
    
    while True:
        
        if option >= 1 and option <= 4:
            return option
        else:
            print('You have entered a wrong input. Please enter a valid input.')
            option = int(input("Please select an option: "))




# Main #######################################################################


#print(menu())
print(load_localfile())


