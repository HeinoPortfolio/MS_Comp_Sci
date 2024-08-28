# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 00:18:35 2024

@author: ntcrw
"""

import pandas as pd

pd.set_option('display.max_rows', 150)

# Question 1 

# Read in the file.
df = pd.read_excel('iris.xlsx')

df2 = pd.read_csv('iris.csv')

#print(df)

# Find the smallest value in the dataframe
min_values = df.min()
print("\nQuestion 1:\n", min_values)


min_values2 = df2.min()
print("Question 1:\n", min_values2)


print("\n\n")
# Question 2
max_values = df.max()
print("\nQuestion 2: \n",max_values)


max_values2 = df2.max()
print("Question 2: \n",max_values2)


#Question #3 
# Check for duplicated rows

df1_dups = df.duplicated()
print("Dataframe 1:",df.duplicated())
#print("Dataframe 2:",df2.duplicated())



# Question 4
print("\nQuestion 4: ",df['sepalLength'].mean())
#print(df2['sepalLength'].mean())

# Question 5
print("\nQuestion 5: ",df['sepalLength'].std())
print("\nQuestion 5: ", df2['sepalLength'].std())


"""
# Question 6
# Draw a boxplot
df.boxplot()
#df2.boxplot()


# Question 7
# Draw a box plot of sepalLenth column
df.boxplot(column='sepalLength')
#df2.boxplot(column='sepalLength')



# save the file
sepalLength_img = df['sepalLength'].plot(kind='box', figsize=(20, 20)
                                         , fontsize=26, title='Sepal Length').get_figure()
sepalLength_img.savefig('box_sepalLength.pdf')


# Question 8
#  Draw a scatter plot of columns sepalLength and pedalLength.

#scatter_img = df[('sepalLength','pedalLength')].plot(kind='scatter', figsize=(20, 20), fontsize=26).get_figure()


scatter_img = df.plot(kind='scatter',figsize=(15, 15), fontsize=20
                      , x='sepalLength',y='petalLength', title=" Petal Length vs Sepal Length ").get_figure()
scatter_img.savefig('scatter.pdf')

"""
# Question 9
#Draw a histogram of column sepalWidth using 20 bins

hist_img = df['sepalWidth'].plot.hist(bins=20, title='Histogram of Sepal Width'
                                      , figsize=(10, 10), fontsize=20
                                      , legend=True
                                      , xlabel= 'Sepal Width').get_figure()

hist_img.savefig('hist.pdf')












