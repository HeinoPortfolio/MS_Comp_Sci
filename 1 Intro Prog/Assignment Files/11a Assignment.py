# -*- coding: utf-8 -*-
"""
Created on Fri May 17 03:36:24 2024

@author: mehei
"""


import re
"""
def translate_to_pirate(english_str)-> str:
   
    # Create a dictionary for the transaltion
    pirate_dict = {'hello': 'ahoy', 'excuse me': 'arr', 'sir':'matey', 'me':'my','the':'th', 'you': 'yer'}
   
    pirate_str = english_str
    # Traverse the string and change to pirate
   
    pirate_str = re.sub(r'er\b', "'r", pirate_str)
   
    for key, value in pirate_dict.items():
       
        pirate_str = re.sub(r'\b' + key + r'\b',value, pirate_str)
   
    #pirate_str = re.sub(r'er\b', "'r", pirate_str)
 """       
 
def translate (user_input):
    
    pirate_dict = {'[Hh]ello': 'ahoy','the':'th','me':'my','you': 'ye'
                   , 'there' : 'thar', 'is' : 'be', '[Ss]tranger': 'scurvy dog'
                   , 'where': 'whar', '[rR]ascal': 'scallywag'
                   , '[oO]ld':'barnacle-covered'}
    
    pirate_str = user_input
    
    for key, value in pirate_dict.items():
       
        pirate_str = re.sub(r'\b' + key + r'\b',value, pirate_str)
    
    pirate_str = re.sub(r'er\b', "'r", pirate_str)
    
    return pirate_str


test_str = "Hello there, Stranger.  Do you know where my brother is, that Old Rascal?"
test_str2 = "hello there, stranger. do you know where my brother is, that old rascal?"


new_pirate_str = translate(test_str2)

print(new_pirate_str)