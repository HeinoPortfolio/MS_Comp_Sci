# -*- coding: utf-8 -*-
"""
Created on Tue May 20 02:41:48 2025

@author: ntcrw

Note:
    
    - uses movie_reviews.csv
    - a zero (0) denotes a negative review and a one (1) denotes a positive 
      review

"""

import pandas as pd

from nltk.tokenize import sent_tokenize
from transformers import pipeline

# -----------------------------------------------------------------------------
# Read in the data from the CSV file with the text review and the associated 
# labels ----------------------------------------------------------------------

reviews_df = pd.read_csv("D:\\Jupyter_Notebooks\\CS654ML_DM\\Data\\movie_reviews.csv")


# Create the pipeling ---------------------------------------------------------

classifier = pipeline('sentiment-analysis', 
                      model='distilbert-base-uncased-finetuned-sst-2-english')


# Use the first 10 reviews for the demo ---------------------------------------

reviews_10 = reviews_df['text'][:10].to_list()

# Show the number of words in each review -------------------------------------

#for review in reviews_10:
    
    #print("\n\nContents: \n", review)
    
    #split_words = review.split()
    
    #print("\n\n",split_words)
    
    #print(len(review.split()))
    
    
# Tokenize the sentences-------------------------------------------------------

sentences = sent_tokenize(reviews_10[0])

#print("\nFirst review: \n",reviews_10[0]) 
#print(len(sentences))


# Create a list of reviews to be used -----------------------------------------

reviews_to_be_used = []

for ind in range (len(reviews_10)):

    sentences = sent_tokenize(reviews_10[ind])

    if len(sentences) > 10:
        review_short = " ".join(sentences[0:10])
    else:
        review_short = " ".join(sentences)
    
    reviews_to_be_used.append(review_short)



# Make Predictions ------------------------------------------------------------

model_predictions_dict = classifier(reviews_to_be_used)

# Extract prediction values from the model_predictions ------------------------
"""
predicted_reviews = [dt['label'] for dt in model_predictions_dict]

movie_review_map = { "NEGATIVE": 0, "POSITIVE": 1 }

predicted_reviews_enc = predicted_reviews.apply(MOVIE_ENCODING)


prediction_scores = [dt['score'] for dt in model_predictions_dict]

"""


# add them to a dataframe 

reviews_10_df = pd.DataFrame()

predicted_reviews = [dt['label'] for dt in model_predictions_dict]


reviews_10_df['Review_text'] = reviews_10
reviews_10_df["Predicted_Reviews"] = [dt['label'] for dt in model_predictions_dict]

movie_review_map = { "NEGATIVE": 0, "POSITIVE": 1 }
reviews_10_df["Predicted_Reviews_Enc"] = reviews_10_df["Predicted_Reviews"].map(movie_review_map)


prediction_scores = [dt['score'] for dt in model_predictions_dict]

reviews_10_df["Predicted_Reviews_Enc"] = prediction_scores


















