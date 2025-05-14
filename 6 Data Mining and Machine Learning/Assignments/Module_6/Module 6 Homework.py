# -*- coding: utf-8 -*-
"""
Created on Wed May 14 01:27:19 2025

@author: ntcrw
"""

true_labels = ['A', 'B', 'A', 'B', 'A', 'A', 'A', 'B','A', 'A', 'A', 'B', 'B',
               'B', 'B', 'B', 'B', 'B', 'A', 'A']

predicted_labels = ['A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 
                    'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B']




num_of_true_A = 0
num_of_true_B = 0

num_of_predicted_A = 0
num_of_predicted_B = 0


#------------------------------------------------------------------------------

for true_item in true_labels:
    
    if true_item == 'A':
        num_of_true_A = num_of_true_A + 1
    else:
        num_of_true_B = num_of_true_B + 1
        
        
# -----------------------------------------------------------------------------

for pred_item in predicted_labels:
    
    if pred_item == 'A':
        num_of_predicted_A = num_of_predicted_A  + 1
    else:
        num_of_predicted_B = num_of_predicted_B+ 1
        
# -----------------------------------------------------------------------------

true_positive = 0
true_negative = 0

false_positive = 0
false_negative = 0

for item in range(len(true_labels)):
    
    if (true_labels[item] == predicted_labels[item]) and (true_labels[item] == 'A'): 
        true_positive = true_positive + 1
        
    elif (true_labels[item] == predicted_labels[item]) and (true_labels[item] == 'B'): 
        true_negative = true_negative + 1
        
    elif (true_labels[item] != predicted_labels[item]) and (true_labels[item] == 'A'): 
        false_negative = false_negative + 1
        
    elif (true_labels[item] != predicted_labels[item]) and (true_labels[item] == 'B'): 
        false_positive = false_positive + 1  
        
    else:
        print("Error!")
        break

print("\nNumber of True Positive: ", true_positive)
print("\nNumber of True Negative: ", true_negative)

print("\nNumber of False Positive: ", false_positive)
print("\nNumber of False Negative: ", false_negative)

total_pred = true_positive  + true_negative + false_positive + false_negative

print("\nTotal number of items: " , total_pred)


print("\n\n\n\n\n\n")


#-----------------------------------------------------------------------------
#
# Question 1:
#
# What is the number of True Positive? 

print("\nQuestion 1: \nNumber of True Positive: ", true_positive)


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 2:
#
# What is the value of False Negative? 

print("\nQuestion 2: \nNumber of False Negative: ", false_negative)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 3:
#
# What is the value of Precision?
#

precision = round((true_positive)/(true_positive+false_positive), 2)

print("\nQuestion 3: \nValue of Precision: ", precision)


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 4:
#
# What is the value of Recall?
#

recall = (true_positive)/(true_positive + false_negative)

print("\nQuestion 4: \nValue of Recall: ", recall)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 5:
#
# What is the value of Accuracy?
#

accuracy =  (true_positive + true_negative)/(true_positive+true_negative +
                                           false_positive+false_negative)


print("\nQuestion 5: \nValue of Accuracy: ", accuracy)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 6:
#
# What is the F1 Score value?
#

f1_score = 2 * ((precision*recall)/(precision+recall))

print("\nQuestion 6: \nValue of F1 Score: ", f1_score)

#------------------------------------------------------------------------------






















