# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:33:07 2025

@author: Matthew Heino
Course: DSCI Course 604 Data Storage and Management
Due Date: April 13, 2025

Purpose of the file:
    
    - Retrieve data from the sample_airbnb and the listingsAndReviews 
    collection:
     
        - Name all the properties in the United States
        - Name all properties with a minimum night stay of 3 nights
        - Name and description of all properties with at least 5 bedrooms
    
"""

# Load the required libraries
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import pprint

# Create the connection client to the database.
conn_str = "mongodb+srv://heinodevs:nelHmIxKERjHMi0T@cluster0.sv7cv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#conn_str2 = "mongodb+srv://bsu1:bsu@cluster0.ahapopo.mongodb.net?retryWrites=true&w=majority"

client = MongoClient(conn_str, server_api=ServerApi('1'))

# connect to the database named sample_airbnb  
airbnb_db = client['sample_airbnb']

# use the ListingsAndReviews collection
listings_coll = airbnb_db['listingsAndReviews']

# Functions 
def US_properties():  
    
    for item in listings_coll.find({"address.country": "United States"},
                               {"_id":0, "name": 1}):
    
        pprint.pprint(item)
        
def three_night_min():
    
    for item in listings_coll.find({"minimum_nights": "3"},
                                   {"_id":0, "name": 1}):
        pprint.pprint(item)
    
def five_bedrooms():    
    for item in listings_coll.find({"beds": {"$gte": 5}}, {"_id":0, "name": 1,
                                                       "description": 1}):
    
        pprint.pprint(item)
    

def menu() -> str:
    
    print("Please enter a menu options from the list below.\n")
    print("1: Name all the properties in the United States")
    print("2: Name all properties with a minimum night stay of 3 nights")
    print("3: Name and description of all properties with at least 5 bedrooms")
    print("4: Quit")
    
    user_choice = input("Enter your choice:   ")

    return user_choice

def main(): 
    
    while True:
        
        option = menu()
      
        # Process the user's choice
        if option == '1':
            print("Name all the properties in the United States")
            US_properties()
        elif option == '2': 
            print("Name all properties with a minimum night stay of 3 nights")
            three_night_min()
        elif option == '3':
            print("Name and description of all properties with at least 5 bedrooms")
            five_bedrooms()
        elif option == '4':
            print("Quit")
            break
        else:
            print("Entered invalid choice. Please make another selection")


if __name__=="__main__":
    main()


























