# -*- coding: utf-8 -*-
"""
Created on Mon May 12 00:49:59 2025

@author: ntcrw
"""

data_i = [70, 51, 37, 94, 58, 9, 95, 95, 99, 38, 45, 63, 51, 22, 19, 50, 3, 68,
          55, 84, 36, 25, 65, 17, 14, 44, 62, 76, 51, 59, 93, 39, 71, 36, 84,
          24, 88, 88, 94, 88, 60, 14, 83, 74, 2, 53, 86, 69, 15, 87, 33, 49, 
          17, 81, 34, 33, 28, 35, 38, 51, 97, 47, 14, 62, 1, 4, 23, 71, 62, 
          40, 20, 36, 76, 84, 90, 96, 62, 36, 69, 34, 43, 53, 44, 47, 51, 13, 
          57, 21, 54, 92, 8, 45, 50, 1, 44, 9, 57, 36, 77, 38]

print(data_i)

print("\n\n\n")

data_s = ['Mango', 'Kiwi', 'Mango', 'Apple', 'Kiwi', 'Apple', 'Banana',
          'Pineapple', 'Mango', 'Apple', 'Pineapple', 'Kiwi', 'Banana',
          'Pineapple', 'Apple', 'Banana', 'Kiwi', 'Kiwi', 'Apple', 'Mango',
          'Pineapple', 'Banana', 'Pineapple', 'Apple', 'Apple', 'Apple',
          'Mango', 'Pineapple', 'Kiwi', 'Kiwi', 'Pineapple', 'Pineapple', 
          'Banana', 'Apple', 'Pineapple', 'Kiwi', 'Kiwi', 'Mango', 'Banana',
          'Kiwi', 'Pineapple', 'Apple', 'Pineapple', 'Kiwi', 'Apple', 'Apple',
          'Banana', 'Pineapple', 'Kiwi', 'Apple', 'Banana', 'Pineapple', 
          'Kiwi', 'Banana', 'Apple', 'Mango', 'Kiwi', 'Banana', 'Mango', 
          'Banana', 'Apple', 'Banana', 'Kiwi', 'Banana', 'Banana', 'Mango', 
          'Apple', 'Apple', 'Mango', 'Apple', 'Pineapple', 'Kiwi', 'Kiwi', 
          'Banana', 'Banana', 'Apple', 'Pineapple', 'Pineapple', 'Apple', 'Kiwi',
          'Mango', 'Kiwi', 'Kiwi', 'Apple', 'Kiwi', 'Pineapple', 'Kiwi', 
          'Pineapple', 'Banana', 'Kiwi', 'Kiwi', 'Kiwi', 'Apple', 'Apple', 
          'Pineapple', 'Pineapple', 'Banana', 'Banana', 'Apple', 'Pineapple']

print(data_s)

print("\n\n\n")


# -----------------------------------------------------------------------------
#
# Question 1:
#  
#  How many values are there in data_i list?
#  
#  - get the number of elements in the list

print("Question 1: \n\nThe number of values in the list is: ", len(data_i))

# -----------------------------------------------------------------------------
# --------------------------------------------------------------------------
# 
# Question 2: 
#    
# What is the difference between the largest value and the smallest value in 
# data_i list?
#
# Find the smallest and the largest value in the list?

min_val = min(data_i)
max_val = max(data_i)

#print("Minimum value: ", min_val)
#print("Maximum value: ", max_val)

# Find the difference 
difference = max_val - min_val

print("\nQuestion 2: \n\nThe difference between the maximum and minimum values: ",
      difference)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 3:
#
# What is the second largest unique value in data_i list?
#
# Find the unique values and then sort them 


unique_vals = list(set(data_i))

sorted_values = unique_vals.copy()

# sort the values in the list

sorted_values.sort(reverse=True)

# print second largest in the list

print("\nQuestion 3: \n\nSecond largest in the list: " , sorted_values[1])

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 4:
#
# How many values are there in data_s list? 
#

print("\nQuestion4: \n\nThe number of values in the list: ", len(data_s))


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 5:
#
# How many distinct fruit names in data_s list?

unique_vals2 = list(set(data_s))

print("\nQuestion 5: \n\nNumber of unique names in list: ", len(unique_vals2))


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 6:
#
# Which fruit name appears most in data_s list? 

freq_dict = {}

for name in unique_vals2:
    
    # get the count 
    count = data_s.count(name)
    
    print("Name: ",name, " Count: ", count)
    
    freq_dict[name] = count
    

sorted_freq = dict(sorted(freq_dict.items(), key=lambda item: item[1], 
                          reverse=True))

#print(freq_dict)

print("\nQuestion 6: \n\n", sorted_freq)















