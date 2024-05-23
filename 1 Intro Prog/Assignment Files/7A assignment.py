# -*- coding: utf-8 -*-
"""
Created on Wed May 15 12:53:54 2024

@author: mehei
"""

# Functions

def list_times_100(orig_list):
    
    list_100 = []
    
    for item in orig_list:
        # Multiply list item by 100
        list_100.append(item * 100)
        
    return list_100


def list_comprehension_100(starting_list):
    
    list_comp_100 = []
    
    # Using a list comprehension
    list_comp_100 =[number *100 for number in starting_list]
    
    
    return list_comp_100
    
    

# main program
number_list = [1,2,3,4,5]


new_100_list = list_times_100(number_list)


print("List: ", new_100_list)

# list comprehension

new_100_list_comp = list_comprehension_100(number_list) 
print("List comprehension: ", new_100_list_comp)