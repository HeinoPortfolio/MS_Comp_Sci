# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:11:41 2024

@author: mehei
"""
def center_vertically(sentence):
    
    max_len = 0
    
    longest = ''
    
    outstring = ''
    
    #Split the string
    word_list = sentence.split()
    
    
    for each_word in word_list:
        if len(each_word) > max_len:
            max_len = len(each_word)
            longest = each_word
    
    
   # print('Longest: ', longest, 'Length: ', word_length)
    
    # center on the screen
    format_string = f'^{max_len}'        #format string
    
    # ouput each word in the list
    for word in word_list:
        # print the word centered
        print(f'{word : {format_string}}')
        
       # outstring += f'{word : {format_string}}' + '\n'
        outstring += f'{word : {format_string}}\n'
        
    return outstring
    
    
test_str = 'Big Ben is the nickname for the Great Bell of the Great Clock of Westminster at the north end of the Palace of Westminster in London England'



#print(test_str)

centered_str = center_vertically(test_str)
print(centered_str)

print("    Big    \n")


""" Good Version

 max_len = 0
    centered_str = ''
    
    # split the string into tokens
    word_list = sentence.split()
    
    # look for the longest word.
    for each_word in word_list:
        if len(each_word) > max_len:
            max_len = len(each_word)
    
    # format for output.
    format_string = f'^{max_len}'     # format string
    
    #build the centered list
    for word in word_list:
        centered_str += f'{word : {format_string}}\n'

    return centered_str

"""
