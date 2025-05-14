# -*- coding: utf-8 -*-
"""
Created on Wed May 14 18:17:02 2025

@author: ntcrw
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 14 18:09:01 2025

@author: ntcrw
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 14 17:28:47 2025

@author: ntcrw


Note:
    
    - cs654_homework8_train_30.csv              -->         Dataset 1
    - cs654_homework8_train_30_labels.csv       -->         Dataset 2
    - cs654_homework8_test_10.csv               -->         Dataset 3
    - cs654_homework8_test_10_labels.csv        -->         Dataset 4
    
"""

import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn import tree

# Pre-question tasks ----------------------------------------------------------
# Read in the data ------------------------------------------------------------

# Read in the training data points---------------------------------------------

training_data = pd.read_csv("cs654_homework8_train_30.csv",
                            header=None).values.tolist()

# Read in the training data labels --------------------------------------------

training_data_labels = pd.read_csv("cs654_homework8_train_30_labels.csv",
                            header=None).values.tolist()

# Read in the test data -------------------------------------------------------

test_data = pd.read_csv("cs654_homework8_train_30.csv",
                            header=None).values.tolist()

# Read in the test data labels ------------------------------------------------

test_data_labels = pd.read_csv("cs654_homework8_train_30_labels.csv",
                               header=None).values.tolist()


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 4:
#
# Use dataset 1 and dataset 2 to construct a regular scikit learn decision 
# tree. Set random_state = 42 and criterion = 'entropy'.
#
# Use dataset 1 and dataset 2 to test the tree's performance. 
#
#What is its accuracy?
#

# Construct the classfier -----------------------------------------------------

# Decision Tree classfier will be created 

dt_clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3,
                                     random_state=42)


# Train or fit the classfier --------------------------------------------------

dt_clf.fit(training_data, training_data_labels)

# Make a prediction using the test data ---------------------------------------


predicted_labels = dt_clf.predict(test_data)

# Compute the model's accuracy ------------------------------------------------

accuracy = accuracy_score(test_data_labels, predicted_labels)

accuracy_dt = dt_clf.score(test_data, test_data_labels)


print("Question 4: The results of model using 'entropy', max_depth=3, and random_state (42) were: ",
      accuracy)


print("Question 4: The results of model using 'entropy', max_depth=3 and random_state (42) were: ",
      accuracy_dt)

