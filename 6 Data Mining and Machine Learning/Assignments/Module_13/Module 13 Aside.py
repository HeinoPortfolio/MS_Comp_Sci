# -*- coding: utf-8 -*-
"""
Created on Fri May 16 03:26:50 2025

@author: ntcrw


Note:  
    
    - There is a total of 200 items or reviews in this example.
    - There are 100 positive reviews 
    - There are 100 negative reviews 
    
    - **reviews_positive_100_words_list** - contains a list of lists in this 
      following format [['mother', 'tells',...], ['some', 'other word' ] ...]



"""



import numpy as np
import pandas as pd
import string

from nltk.corpus import stopwords
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score


df = pd.read_csv("D:\\Jupyter_Notebooks\\CS654ML_DM\\Data\\movie_reviews.csv")



# Methods ---------------------------------------------------------------------

def my_clean_words(s):
    
    all_words = []
    
    review = s.translate(str.maketrans('','', string.punctuation))
    
    words = review.split()
    
    for w in words:
        
        w = w.lower()
        
        if w not in english_stops:
            
            all_words.append(w)
            
    return all_words

#------------------------------------------------------------------------------


# sort the list -------------------------------------------
df.sort_values(by = 'label', ascending=False, inplace=True)


# Save 100 positive 100 negative reviews --------------------------------------

df_positive_100 = df.head(100)

df_negative_100 = df.tail(100)


# Save the text of the reviews into lists -------------------------------------

reviews_positive_100 = df_positive_100.iloc[ : , 0].to_list()

reviews_negative_100 = df_negative_100.iloc[:, 0].to_list()


# Remove the stop words and clean the lists. ----------------------------------

english_stops = stopwords.words('english')

# Clean the reviews -----------------------------------------------------------
# -----------------------------------------------------------------------------

# Positive reviews ------------------------------------------------------------

reviews_positive_100_words = []

reviews_positive_100_words_list=[]

for review in reviews_positive_100:
    
    words_cleaned = my_clean_words(review)
    
    reviews_positive_100_words_list.append(words_cleaned)
    
    for w in words_cleaned:
        reviews_positive_100_words.append(w)


positive_words_set = set(reviews_positive_100_words )


# Negative reviews ------------------------------------------------------------

reviews_negative_100_words = []

reviews_negative_100_words_list=[]

for review in reviews_negative_100:
    
    words_cleaned = my_clean_words(review)
    reviews_negative_100_words_list.append(words_cleaned)
    
    for w in words_cleaned:
        reviews_negative_100_words.append(w)

negative_words_set = set(reviews_negative_100_words)

#------------------------------------------------------------------------------
# Distinct words from the lists -----------------------------------------------

all_distinct_words = set(reviews_negative_100_words+reviews_positive_100_words)

# Create an attribute/ feature list ------------------------------------------

attribute_words = list( set(reviews_negative_100_words +
                            reviews_positive_100_words))


#------------------------------------------------------------------------------
# Transform positive reviews into one-hot encoding ----------------------------

positive_vectors = []


for ind in range(len(reviews_positive_100_words_list)):
    
    vector_p = []
    
    for ind2 in range(len(attribute_words)):
        
        if attribute_words[ind2] in reviews_positive_100_words_list[ind]:
            
            vector_p.append(1)
        else:
            
            vector_p.append(0)
            
    positive_vectors.append(vector_p)


# Transform negative reviews into one-hot encoding ----------------------------

negative_vectors = []


for ind in range(len(reviews_negative_100_words_list)):
    
    vector_n = []
    
    for ind2 in range(len(attribute_words)):
        
        if attribute_words[ind2] in reviews_negative_100_words_list[ind]:
            
            vector_n.append(1)
        else:
            
            vector_n.append(0)
            
    negative_vectors.append(vector_n)



# -----------------------------------------------------------------------------
# Create class labels ---------------------------------------------------------


positive_negative_labels =[]

for i in range(100):
    positive_negative_labels.append(1)

for i in range(100):
    positive_negative_labels.append(0)
    

#-----------------------------------------------------------------------------    
# Convert into numpy array ----------------------------------------------------

X = np.array(positive_vectors + negative_vectors) 


#------------------------------------------------------------------------------
# Convert the labels ----------------------------------------------------------

y = np.array(positive_negative_labels)


# Split the data into training and test sets ----------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5,
                                                    random_state = 42)




#------------------------------------------------------------------------------
# Create a MultinomialNB classifier -------------------------------------------




nb_classifier_model = MultinomialNB()

nb_classifier_model.fit(X_train, y_train)


y_train_pred = nb_classifier_model.predict(X_train)
y_test_pred = nb_classifier_model.predict(X_test)


# Accuracy --------------------------------------------------------------------


# Using the training data -----------------------------------------------------

accuracy_train = accuracy_score(y_true = y_train , y_pred= y_train_pred)


# Using the testing data ------------------------------------------------------

accuracy_test = accuracy_score(y_true = y_test, y_pred = y_test_pred)



NB_model = MultinomialNB()

scores = cross_val_score(NB_model, X, y, cv = 2)


print("Cross Validation Scores: ", scores)

print("Average CV Score: ", scores.mean())

print("Number of CV Scores used in Average: ", len(scores)) 


print(cross_val_score(nb_classifier_model, X, y, cv = 5))



































