# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:12:08 2025

@author: Matthew Heino
"""

from pymongo import MongoClient

class AtlasClient ():

   def __init__ (self, altas_uri, dbname):
       self.mongodb_client = MongoClient(altas_uri)
       self.database = self.mongodb_client[dbname]

   ## A quick way to test if we can connect to Atlas instance
   def ping (self):
       self.mongodb_client.admin.command('ping')

   def get_collection (self, collection_name):
       collection = self.database[collection_name]
       return collection

   def find (self, collection_name, filter = {}, limit=0):
       collection = self.database[collection_name]
       items = list(collection.find(filter=filter, limit=limit))
       return items



ATLAS_URI = "mongodb+srv://heinodevs:nelHmIxKERjHMi0T@cluster0.sv7cv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


DB_NAME = 'sample_mflix'
COLLECTION_NAME = 'embedded_movies'

atlas_client = AtlasClient (ATLAS_URI, DB_NAME)
atlas_client.ping()


print ('Connected to Atlas instance! We are good to go!')


movies = atlas_client.find (collection_name=COLLECTION_NAME, limit=5)
print (f"Found {len (movies)} movies")

# print out movie info
for idx, movie in enumerate (movies):
   print(f'{idx+1}\nid: {movie["_id"]}\ntitle: {movie["title"]},\nyear: {movie["year"]}\nplot: {movie["plot"]}\n')