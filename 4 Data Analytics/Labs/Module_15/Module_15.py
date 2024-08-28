# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:04:26 2024

@author: ntcrw

Notes:
    1) x values are:
    2) y values are:
    3) Number of rows:       1000


"""

import numpy as np
#import math
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import mean_absolute_error

#sns.lmplot(x='one',y='two',data=df,fit_reg=True)


flights_df = pd.read_csv('flights_1000.csv')


depDelay_x = np.array(flights_df['DepDelay']).reshape(-1, 1)
arrDelay_y = np.array(flights_df['ArrDelay']).reshape(-1, 1)


max_val_dep = max(flights_df['DepDelay'])
min_val_dep = min(flights_df['DepDelay'])

max_val_arr = max(flights_df['ArrDelay'])
min_val_arr = min(flights_df['ArrDelay'])

# plot a graph
#plots = flights_df.plot(kind='scatter', x='DepDelay', y='ArrDelay')
#sns.lmplot(data=flights_df, x='DepDelay', y='ArrDelay', fit_reg=True)

#plot.plot(depDelay_x, arrDelay_y)



# create a linear regression
lin_reg = LinearRegression()

# Fit the data to the linear regression model
lin_reg.fit(depDelay_x, arrDelay_y)

#lin_reg.fit(arrDelay_y, depDelay_x )

# ============================================================================
# Question 1
#
# Which description in the following about the coefficient value (w1) is 
# correct?
#
# ============================================================================ 
w1_coef = lin_reg.coef_

print("Q1) Coefficient value: ", w1_coef)

# ============================================================================


# ============================================================================
# Question 2
#
# Which description in the following about the intercept value (w0) is 
# correct?
#
# ============================================================================ 

w0_intercept = lin_reg.intercept_

print("Q2) Intercept value: ",w0_intercept)

# ============================================================================


# =============================================================================
# Question 3
#
# Which description about the mean absolute error value of this model is 
# correct?
#
#==============================================================================

# Predict some values for ArrDelay.

predicted_ArrDel = lin_reg.predict(depDelay_x) 

true_values = arrDelay_y

abs_error = mean_absolute_error(true_values, predicted_ArrDel)

print("Q3) Mean absolute error value: ",abs_error)


# =============================================================================


























