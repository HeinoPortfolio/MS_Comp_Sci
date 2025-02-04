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


# Create the connection client to the database.
conn_str = "mongodb+srv://heinodevs:nelHmIxKERjHMi0T@cluster0.sv7cv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#conn_str2 = "mongodb+srv://bsu1:bsu@cluster0.ahapopo.mongodb.net?retryWrites=true&w=majority"

client = MongoClient(conn_str, server_api=ServerApi('1'))

# connect to the database named sample_mflix  
mflix_db = client['sample_mflix']

# use the movies collection
listings_coll = mflix_db['movies']

# Functions 
def drama_2007():
    """ Returns the title of all movies released in 20027 
    
    Parameters:
        
        None
        
    Returns:
        
        list: List of all title of all movies released in 20027
        
    """
    
    movies =[]
    
    for item in listings_coll.find({"$and":[{ "genres": "Drama"},
                                            {"year": 2007}]},
                                   {"_id":0, "title":1}):
        movies.append(item)
    
    return movies
    
def pg_13():
    
    """ Returns the title of all movies with PG13 rating and won at 
        least 3 awards
    
    Parameters:
        
        None
        
    Returns:
        
        list: List of all title of all movies with PG13 rating and won at 
            least 3 awards
        
    """
    
    movies = []
    
    for item in listings_coll.find({"$and":[{"rated": "PG-13"},
                                            {"awards.wins": {"$gte": 3}}]},
                                   {"_id":0, "title":1}):
    
        movies.append(item)

    return movies

def seven_rating_movie(): 
    
    """ Returns title of all movies with with an IMDB rating of 7 or more
    
    Parameters:
        
        None
        
    Returns:
        
        list: List of all titles of all movies with with an IMDB rating of 
        7 or more
        
    """
    movies = []
    
    for item in listings_coll.find({"imdb.rating": {"$gte": 7}},
                               {"_id":0, "title": 1}):
    
        movies.append(item)

    return movies

def print_title(movies):
    
    """ print title of the movies
    
    Parameters:
        
        movies: list of dictionaries
        
    Returns:
        
        None
        
    """
    for movie in movies:
        print(movie['title'])
    
   
def menu() -> str:
    
    """ Defnines the menu options """
    
    print("\n\nPlease enter a menu options from the list below.\n")
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
            print_title(seven_rating_movie())
        elif option == '2': 
            print("Title of drama (genre) movies released in 2007")
            print_title(drama_2007())
        elif option == '3':
            print("Title of PG-13 (rated) movies that have won at least 3 awards")
            print_title(pg_13())
        elif option == '4':
            print("Quit")
            break
        else:
            print("Entered invalid choice. Please make another selection")


if __name__=="__main__":
    
    main()
