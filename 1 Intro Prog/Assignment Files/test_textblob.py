# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:37:23 2024

@author: mehei
"""

from textblob import TextBlob

my_text = TextBlob("I am reading a blog post on Medium. I am loving it!")

print(my_text.words)

print(my_text.sentences)

print(my_text.tags)