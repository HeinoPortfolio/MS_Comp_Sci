# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:33:07 2025

@author: Matthew Heino
Course: DSCI Course 604 Data Storage and Management
Due Date: April 13, 2025

Purpose of the file:
    
    - Retrieve data from the sample_mflix and the movies collection:
     
        - Title of movies with an imdb rating of 7 or more
        - Title of drama (genre) movies released in 2007
        - Title of PG-13 (rated) movies that have won at least 3 awards
    
"""

# Load the required libraries
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import pprint

# Create the connection client to the database.
conn_str = "mongodb+srv://heinodevs:nelHmIxKERjHMi0T@cluster0.sv7cv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#conn_str2 = "mongodb+srv://bsu1:bsu@cluster0.ahapopo.mongodb.net?retryWrites=true&w=majority"

client = MongoClient(conn_str, server_api=ServerApi('1'))

# print a listing of all the database names to check the connection
#print(client.list_database_names())

# connect to the database named sample_mflix  
airbnb_db = client['sample_mflix']

# use the movies collection
listings_coll = airbnb_db['movies']

# Check to see if there is a connection to the database and the collection
#listings_tmp = listings_coll.find_one()
#print(listings_tmp)
#pprint.pprint(listings_tmp)


# Functions 
def seven_rating_movie():  
    
    for item in listings_coll.find({"imdb.rating": {"$gte": 7}},
                               {"_id":0, "title": 1}):
    
        pprint.pprint(item)


def drama_2007():
    
    for item in listings_coll.find({"$and":[{ "genres": "Drama"},
                                            {"year": 2007}]},
                                   {"_id":0, "title":1, "year":1}):
        pprint.pprint(item)
    
def pg_13():
    
    for item in listings_coll.find({"$and":[{"rated": "PG-13"},
                                            {"awards.wins": {"$gte": 3}}]},
                                   {"_id":0, "title":1, "rated":1,
                                    "awards.wins": 1}):
    
        pprint.pprint(item)
    
def menu() -> str:
    
    print("Please enter a menu options from the list below.\n")
    print("1: Title of movies with an imdb rating of 7 or more")
    print("2: Title of drama (genre) movies released in 2007")
    print("3: Title of PG-13 (rated) movies that have won at least 3 awards")
    print("4: Quit")
    
    user_choice = input("Enter your choice:   ")

    return user_choice

def main(): 
    
    while True:
        
        option = menu()
      
        # Process the user's choice
        if option == '1':
            print("Title of movies with an imdb rating of 7 or more")
            seven_rating_movie()
        elif option == '2': 
            print("Title of drama (genre) movies released in 2007")
            drama_2007()
        elif option == '3':
            print("Title of PG-13 (rated) movies that have won at least 3 awards")
            pg_13()
        elif option == '4':
            print("Quit")
            break
        else:
            print("Entered invalid choice. Please make another selection")


if __name__=="__main__":
    main()
