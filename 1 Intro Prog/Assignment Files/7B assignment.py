# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:07:29 2024

@author: mehei
"""

def roman_to_decimal(roman_str):
    
    
    roman_letters = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100 }
    
    to_decimal = 0
    
    for char in range(0, len(roman_str)):
        
        key = roman_str[char]
        if key in roman_letters:
            to_decimal = to_decimal + roman_letters[key]
    
    
    return to_decimal


# main ******************************************

rom_str = 'ILIC'

# call to the roman_to_decimal
converted_to_decimal = roman_to_decimal(rom_str)
print(converted_to_decimal)

