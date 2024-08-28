# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 04:04:47 2024

@author: ntcrw
"""

import pandas as pd
from datetime import datetime

df = pd.read_csv('amazon_10_years.csv')

print(df.head())
print(df.size)


# Question 1
# Which date has the largest volume number (date format as year-month-day)?

max_vol = df['Volume'].max()

date1 = df[df.Volume == max_vol]['Date']
print("\nQuestion 1: ", date1)


# Question 2
#  Which date has the lowest open value number?

low_open = df['Open'].min()
low_date = df[df.Open == low_open]['Date']
print("\nQuestion 2: ", low_date)


# Question 3
# Which date has the largest positive difference between open 
# and close prices? (close price is higher than open price)  

q3_df = df[['Date','Open', 'Close']].copy()

q3_df['Variance'] = q3_df['Close'] - q3_df['Open']

print(q3_df.head())

max_dif = q3_df[q3_df.Variance == q3_df.Variance.max()]['Date']
print("\nQuestion 3:",max_dif)

# Question 4 
# Which date has the largest negative difference between open and close 
# prices? (close price is lower than open price) 
min_dif = q3_df[q3_df.Variance == q3_df.Variance.min()]['Date']
print("\nQuestion 4:",min_dif)



# Question 5 
# Which year has the largest total volume number?
q5_df = df[['Date','Volume']].copy()
print(q5_df.head())


#print(q5_df.dtypes)

q5_df['Year'] = pd.DatetimeIndex(q5_df['Date']).year

#print(q5_df.dtypes)

total_volume = q5_df.groupby(['Year'])['Volume'].sum()

#print(total_volume)
#print(type(total_volume))

#tot_year = total_volume[total_volume[].max['Date']

tot_year = total_volume[total_volume == total_volume.max()]
print(str(tot_year.index))


# Question 6 
# Which weekday has the highest average volume number?
q6_df = q5_df.copy()
q6_df.drop('Year', axis=1, inplace=True)
print(q6_df.head())

#
#q6_df['Weekday'] = pd.DatetimeIndex(q6_df['Date']).day_of_week.strft

q6_df['Weekday'] = pd.DatetimeIndex(q6_df['Date']).strftime('%A')

print(q6_df.dtypes)

#q6_df['Weekday'] =  q6_df['Day'].

#q6_df['Weekday']

print(q6_df.head())

high_ave_day  = q6_df.groupby(['Weekday'])['Volume'].mean()

print("\nQuestion 6:",high_ave_day)

# Question 7


#Question 7
#Create a time series line chart using Date and Close columns.
#time_series = pd.Series([df['Close']], index=df['Date'])

#time_series_line = df.plot.line(x='Date', y='Close').get_figure()
#time_series_line.savefig('time_series.pdf')


# Question 8
#Create a time series line chart using Date and Close columns,
#Also add another line using rolling mean with window size 250. 

q7_df = df[['Date','Close']].copy()

print(q7_df)

# Creating a moving average with window size= 250.
q7_df['Moving Avg'] = q7_df['Close'].rolling(window=250).mean()


# Create the graph
mov_line = q7_df.plot.line(x='Date', y=['Close', 'Moving Avg']).get_figure()
mov_line.savefig('mov_lines.pdf')


# Question 9
# Create a time series line chart using Date and Close column .Also add 
# another line using rolling std with window size 250. 

q7_df['Moving Std'] = q7_df['Close'].rolling(window=250).std()


mov_line2 = q7_df.plot.line(x='Date', y=['Close', 'Moving Avg','Moving Std']).get_figure()
mov_line2.savefig('mov_lines_std.pdf')























