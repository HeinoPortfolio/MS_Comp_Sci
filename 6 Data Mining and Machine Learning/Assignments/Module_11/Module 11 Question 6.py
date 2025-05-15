# -*- coding: utf-8 -*-
"""
Created on Thu May 15 04:08:30 2025

@author: ntcrw
"""

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

#------------------------------------------------------------------------------
# Pre-question work -----------------------------------------------------------

transactions = [['A', 'B', 'C'], ['A', 'C'], ['A', 'D'], ['B','E','F']]


# Convert to string
transactions = [[str(item) for item in transaction] for transaction in transactions]

# Create the transaction encoder ----------------------------------------------
tran_enc = TransactionEncoder()

# Create transaction array with each elment -----------------------------------
te_array = tran_enc.fit(transactions).transform(transactions)
    
# Create a dataframe to show the results of the encoding / transformation -----

    
encoded_transactions_df = pd.DataFrame(te_array, columns=tran_enc.columns_)

#print(encoded_transactions_df)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#
# Question 6:
#
# With min_support = 0.25, what is the confidence of rule B->(E,F)? 
# 

# Find frequent itemsets with minimum support of 0.2 -------------------------
frequent_itemsets = apriori(encoded_transactions_df, min_support=0.25, 
                            use_colnames=True)
    

#print("Frequent item sets: ", frequent_itemsets)


# Generate association rules with minimum confidence of 0.5 -------------------
   
assoc_rules = association_rules(frequent_itemsets, metric="confidence", 
                          min_threshold=0)

#print("\n Question1: \n", rules)
