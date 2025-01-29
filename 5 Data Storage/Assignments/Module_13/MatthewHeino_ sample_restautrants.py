# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:33:07 2025

@author: Matthew Heino
Course: DSCI Course 604 Data Storage and Management
Due Date: April 13, 2025

Purpose of the file:
    
    - Retrieve data from the sample_restaurants and the restaurants collection:
     
        - Name of all restaurants in Brooklyn (borough)
        - Name and borough of all American cuisine restaurants in Queens 
        (borough)
    
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
airbnb_db = client['sample_restaurants']

# use the ListingsAndReviews collection
listings_coll = airbnb_db['restaurants']

# Functions 
def brooklyn_rests():  
    
    for item in listings_coll.find({"borough": "Brooklyn"},
                               {"_id":0, "name": 1, "borough":1}):
    
        pprint.pprint(item)
        
def american_cuisine():
    
    for item in listings_coll.find({"$and":[{"cuisine": "American"},{"borough": "Queens"}]},
                                   {"_id":0, "name": 1,  "borough":1}):
        pprint.pprint(item)
      
def menu() -> str:
    
    print("Please enter a menu options from the list below.\n")
    print("1: Name of all restaurants in Brooklyn (borough)")
    print("2: Name and borough of all American cuisine restaurants in Queens (borough)")
    print("3: Quit")
    
    user_choice = input("Enter your choice:   ")

    return user_choice

def main(): 
    
    while True:
        
        option = menu()
      
        # Process the user's choice
        if option == '1':
            print("Name of all restaurants in Brooklyn (borough)")
            brooklyn_rests()
        elif option == '2': 
            print("Name all properties with a minimum night stay of 3 nights")
            american_cuisine()
        elif option == '3':
            print("Quit")
            break
        else:
            print("Entered invalid choice. Please make another selection")


if __name__=="__main__":
    main()


























