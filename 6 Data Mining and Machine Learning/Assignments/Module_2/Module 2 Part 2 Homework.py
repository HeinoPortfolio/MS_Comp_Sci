# -*- coding: utf-8 -*-
"""
Created on Mon May 12 02:27:35 2025

@author: ntcrw
"""

import pandas as pd
import numpy as np

fin = open("cs654_homework2_dataset2.txt")


courses_raw = []

for row in fin:
    
   courses_raw.append(row)
   
fin.close()

print(courses_raw)


course_entries = []


for course in courses_raw:
    
    stripped = course.strip().split(",")
    
    
    course_list = []
    
    for cr in stripped:
        
        course_list.append(cr.strip())
        
    course_entries.append(course_list)

print(course_entries)


unique_courses = []

for course in course_entries:
    
    for course_name in course:
        
        if course_name not in unique_courses:
            
            unique_courses.append(course_name)
            
print("\nUnique courses before the sort: ", unique_courses)

unique_courses.sort()

print("\nUnique courses after sort: \n", unique_courses)


# -----------------------------------------------------------------------------
# 
# Question 5:
#
# How many distinct course titles are there in this dataset?
#

print("\n\nQuestion 5: \n\n Distinct course title counts: ", len(unique_courses))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# Question 6:
#
# Use the distinct course titles as column names, and convert each student’s 
# course list as a row of 1/0 correspondingly. That is, 1 for a particular 
# columns means that course exists in the student’s course list, and 0 
# means the student does not take that class. 
#
# If we add up all the 1/0 entries in the array, what is the sum value?


# -----------------------------------------------------------------------------

final_table = []

for i in range (len(course_entries)):

    result = []
    
    for name in unique_courses:
        if name in course_entries[i]:
            result.append(1)
        else:
            result.append(0)
            
    final_table.append(result)

print("\n\nFinal Table: ", final_table)

# View the table as  dataframe with labels

student_courses_df = pd.DataFrame(final_table,columns= unique_courses)

print("\n")
print(student_courses_df)


# sum the data frame

total_sum = student_courses_df.sum().sum()

total_sum_np = np.sum(student_courses_df.values)


print("\nQuestion 6: \n")

print("\n The total or sum of the entries is: ", total_sum)
print("\n The total or sum of the entries is (using numpy array): ", total_sum_np)









