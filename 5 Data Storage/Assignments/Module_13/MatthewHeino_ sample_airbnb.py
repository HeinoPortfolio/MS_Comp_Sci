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
    
    """ Returns the name of all US properties 
    
    Parameters:
        
        None
        
    Returns:
        
        list: List of all names of US properties 
        
    """
    props = []
    
    for item in listings_coll.find({"address.country": "United States"},
                               {"_id":0, "name": 1}):
    
        props.append(item)
        
    return props
        
def three_night_min():
    """ Returns the name of all properties with a minimum of 3 night stay 
    
    Parameters:
        
        None
        
    Returns:
        
        list: List of all names of properties with a minimum 3 night stay 
        
    """
    
    props = []
    
    for item in listings_coll.find({"minimum_nights": "3"},
                                   {"_id":0, "name": 1}):
       props.append(item)
    
    return props

def five_bedrooms():  
    """ Returns the name of all properties and description with at least 5 
        bedrooms 
    
    Parameters:
        
        None
        
    Returns:
        
        list: List of all names of of all properties and description with at 
            least 5 bedrooms properties 
        
    """
    
    props = []
    
    for item in listings_coll.find({"beds": {"$gte": 5}}, {"_id":0, "name": 1,
                                                       "description": 1}):
    
        props.append(item)
    
    return props

def print_information(properties):
    
    """ prints all the infomation in the dictionary
    
    Parameters:
        
        properties: list of dictionaries
        
    Returns:
        
        None
        
    """
    for property in properties:
        print("\n", property['name'])
        if "description" in property:
            print(property['description'])


def menu() -> str:
    
    """ Defnines the menu options """
    
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
            print_information(US_properties())
        elif option == '2': 
            print("Name all properties with a minimum night stay of 3 nights")
            print_information(three_night_min())
        elif option == '3':
            print("Name and description of all properties with at least 5 bedrooms")
            print_information(five_bedrooms())
        elif option == '4':
            print("Quit")
            break
        else:
            print("Entered invalid choice. Please make another selection")


if __name__=="__main__":
    
    main()


























