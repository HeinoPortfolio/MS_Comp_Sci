# -*- coding: utf-8 -*-
"""
Created on Tue May 20 03:41:11 2025

@author: ntcrw


Notes:
    
    - Dataset 1 and dataset 2 consist of movie reviews and their true 
      labels (1:positive, 0:negative).

    - Will use the following classifier from Hugging Face to predict each 
      movie review's sentiment.
      
    - Uses files:
        
        - movie_reviews_500_negative.csv
        - movie_reviews_500_positive.csv

Note A: 
    
    Each prediction contains a label and a score. For instance, 
    {'label': 'POSITIVE', 'score': 0.9995930790901184}
    
Note B:

    - This program may take few moments to run based on the hardware employed 
      on the computer.  
    
    - Can take up to three minutes


"""

import pandas as pd

from transformers import pipeline

#------------------------------------------------------------------------------
# Prequestion tasks------------------------------------------------------------

# Read in the data from the positive reviews ----------------------------------

reviews_df = pd.read_csv("movie_reviews_500_negative.csv")

# Extract the text from the reviews dataframe ---------------------------------

reviews_to_be_used = reviews_df['text'].to_list()


# Create the pipeline ---------------------------------------------------------

classifier = pipeline('sentiment-analysis', 
                      model='distilbert-base-uncased-finetuned-sst-2-english')


# Make Predictions ------------------------------------------------------------

model_predictions_dict = classifier(reviews_to_be_used)


# Extract prediction values from the model_predictions ------------------------
# add the data to the dataframe -----------------------------------------------


predicted_reviews = [dt['label'] for dt in model_predictions_dict]


reviews_df["Predicted_Reviews"] = [dt['label'] for dt in model_predictions_dict]

movie_review_map = { "NEGATIVE": 0, "POSITIVE": 1 }
reviews_df["Predicted_Reviews_Enc"] = reviews_df["Predicted_Reviews"].map(movie_review_map)


prediction_scores = [dt['score'] for dt in model_predictions_dict]

reviews_df["Predicted_Reviews_Scores"] = prediction_scores


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 7
#
# For the correct negative predictions (true label is negative, and prediction 
# is also negative), 
#
# What is the average score?
#

neg_neg_pred_df = reviews_df[(reviews_df['label'] == 0) &
                             (reviews_df['Predicted_Reviews_Enc'] == 0)]

# Compute the average of the score column

score_col_avg = neg_neg_pred_df['Predicted_Reviews_Scores'].mean()

print("\n\nQuestion 7: \n")
print("\nThe average score for both a negative label and negative prediction is: \n",
      score_col_avg)

print("\n\nThe average score for both a positive label and positive prediction is [rounded]: \n",
      round(score_col_avg, 2))











