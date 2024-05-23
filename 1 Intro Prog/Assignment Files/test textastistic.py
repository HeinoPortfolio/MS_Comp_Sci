# -*- coding: utf-8 -*-
"""
Created on Tue May 21 01:08:32 2024

@author: mehei
"""

from textatistic import Textatistic

text_sample = 'There were a king with a large jaw and a queen with a plain face, on the throne of England; there were a king with a large jaw and a queen with a fair face, on the throne of France. In both countries it was clearer than crystal to the lords of the State preserves of loaves and fishes, that things in general were settled for ever.'



# Create a Textatistic object
s = Textatistic(text_sample)

#print(s.counts)


# print sentence count

print(s.sent_count) 

print(s.dalechall_score)

print(s.flesch_score)