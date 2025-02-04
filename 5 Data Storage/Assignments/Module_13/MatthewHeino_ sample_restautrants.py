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
restaurants_db = client['sample_restaurants']

# use the ListingsAndReviews collection
listings_coll = restaurants_db['restaurants']


# Functions 
def american_cuisine():
    """ Returns the name and borough of American cuisine restaurants in Queens 
    
    Parameters:
        None
        
    Returns:
        list: List of restaurant names and the borough 
        
    """
    
    rests = []
    
    for item in listings_coll.find({"$and":[{"cuisine": "American"}, {"borough": "Queens"}]},
                                   {"_id":0, "name": 1,  "borough":1}):
        
      rests.append(item)
      
    return rests

def brooklyn_rests():
    """ Returns a list of restaurant names in Brooklyn
    
    Parameters:
        
        None
        
    Returns:
        
        list: List of restaurant names
    """
    
    rests = []
    
    for item in listings_coll.find({"borough": "Brooklyn"},
                               {"_id":0, "name": 1}):
    

        rests.append(item)
        
    return rests    
      
def print_information(restaurants):
    
    """ prints all the infomation in the dictionary
    
    Parameters:
        
        properties: list of dictionaries
        
    Returns:
        
        None
        
    """
    for restaurant in restaurants:
        if  restaurant ['name'] != "": 
            print(restaurant ['name'])
        else:
            print("No Name Given!")
        if "borough" in restaurant:
            print(restaurant ['borough'])


def menu() -> str:
    """ Defnines the menu options """
    
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
            print_information(brooklyn_rests())
        elif option == '2': 
            print("Name and borough of all American cuisine restaurants in Queens (borough)")
            print_information(american_cuisine())
        elif option == '3':
            print("Quit")
            break
        else:
            print("Entered invalid choice. Please make another selection")


if __name__=="__main__":
    
    main()


























