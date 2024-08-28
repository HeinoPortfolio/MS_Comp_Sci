# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 02:04:15 2024

@author: ntcrw
"""
import pandas as pd


df = pd.read_csv('video_rental.csv')

#print(df)


# Question 1
#   How many rows and column does this dataset have
print("Rows and Columns", df.shape)
print("\n")


# Question 2
by_gender = df.groupby("Gender")['Gender'].count()
print(by_gender)


# Question 3 
# What is the average income of the female customers.
avg_inc_female = df.groupby("Gender")['Income'].mean()
print(avg_inc_female)

print("\n")
"""
avg_inc_female2 = df[df['Gender'] == 'F']
#print(avg_inc_female2)
#print(type(avg_inc_female2))

avg_inc = avg_inc_female2['Income'].mean()
print(avg_inc)
"""

# Question 4
# For male customers who love Drama genre, what is the oldest age?
drama_male = df[(df['Gender'] == "M") & (df['Genre'] == 'Drama')]['Age'].max()

print("\n",drama_male)

# Question 5
# What is the youngest age of male customers?

youngest_male = df[df['Gender'] == 'M']['Age'].min()
print("\n", youngest_male)

# 
# Question 6
# What is the average age among female customers who love Drama movies?
drama_female = df[(df['Gender'] == "F") & (df['Genre'] == 'Drama')]['Age'].mean()
print("\n", drama_female)



# Question 7
# Use the Genre column to draw a bar chart.
#bar_genre = df['Genre'].value_counts().plot(kind='bar').get_figure()
#bar_genre.savefig('bar_genre.pdf')

"""
# Question 9 
# Use the Genre column to draw a pie chart.
count_1 =  df.groupby(['Genre'])['Genre'].count()
print(count_1)

count_img = df.groupby(['Genre'])['Genre'].count().plot(kind='pie'
                                                        , autopct='%1.0f%%'
                                                        ,ylabel="").get_figure()

count_img.savefig('pie_genre.pdf')
"""


# Question 10
# Use the Genre, Gender, and Age columns to draw 
# a bar chart that shows the average ages of Male and Female customers 
# separately on each movie genre.

#avg_img = df.groupby(['Genre', 'Gender'])['Age'].mean().get_figure()


genre_summary = df.groupby(['Genre','Gender'])['Age'].mean().unstack()

#print(genre_summary)

avg_img = genre_summary.plot(kind='bar').get_figure()
avg_img.savefig('avg_genre.pdf')



















