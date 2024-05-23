# -*- coding: utf-8 -*-
"""
Created on Thu May 16 00:14:40 2024

@author: mehei
"""

def replace_the_with_smile(sentence):
    
    grinning_face = 0x1F600 # regular grinning face
    
    smile_string = sentence.replace('the', f'{grinning_face:c}')
    
    
    return smile_string
    
    
def replace_4_letter_words(sentence):
   # print('in 4')
    
    grinning_face = 0x1F600
    
    #word_list = []
    
    emoji_str = sentence
    
    for word in sentence.split():
        
        if(len(word) == 4):
            # replace the word with an emoji
            emoji_str = emoji_str.replace(word, f'{grinning_face:c}')
            grinning_face += 1
    
    return emoji_str



test_str = "This line will test your solution"
test_str2 = 'She sell sea shells at the sea shore'

emojied_str = replace_4_letter_words(test_str)


print(emojied_str)
print(type(emojied_str))

"""
new_string = replace_the_with_smile(test_str)

print(new_string)
"""
