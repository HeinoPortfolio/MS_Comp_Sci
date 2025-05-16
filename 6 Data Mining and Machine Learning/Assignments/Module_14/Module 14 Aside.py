# -*- coding: utf-8 -*-
"""
Created on Fri May 16 18:26:26 2025

@author: ntcrw
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier

import pandas as pd

df1 = pd.read_csv("D:\\Jupyter_Notebooks\\CS654ML_DM\\Data\\iris.csv")


X = df1.drop(["species"],axis=1).values

df1['species'] = df1['species'].map({'Iris-setosa':0,'Iris-versicolor':1,
                                     'Iris-virginica':2})




# Y is the encoded values for the types of irises -----------------------------

y = df1["species"].values


# Split the training data into testing and training ---------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# Create the model ------------------------------------------------------------

clf = MLPClassifier(max_iter=10000, random_state=42)


# Training / learning the model -----------------------------------------------

clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)



print(accuracy_score(y_test, y_pred))































