/*
		Matthew Heino
		Assignment # 7
		
*/

/*
sample_airbnb : listingsAndReviews
    • Name of all properties in the United States
    • Name of all properties with a minimum night stay of 3
    • Name and description of all properties with at least 5 bedrooms
	
*/

// Name of all properties in the United States
db.listingsAndReviews.find({"address.country": "United States"}, {address:1})
db.listingsAndReviews.find({"address.country": "United States"}, {name:1, _id:0})

// Name of all properties with a minimum night stay of 3
db.listingsAndReviews.find({minimum_nights: "3"}, {name:1, _id:0})

//Name and description of all properties with at least 5 bedrooms
db.listingsAndReviews.find({beds: {$gte: 5}}, {_id:0, name:1, beds:1, description: 1})

/*
sample_mflix : movies
    • Title of movies with an imdb rating of 7 or more
    • Title of drama (genre) movies released in 2007
    • Title of PG-13 (rated) movies that have won at least 3 awards
	
*/

//Title of movies with an imdb rating of 7 or more
db.movies.find({"imdb.rating": {$gte: 7}}, {_id: 0, title:1, "imdb.rating": 1})

// Title of drama (genre) movies released in 2007
db.movies.find({$and:[{ genres: "Drama"},{year: 2007}]}, {_id:0, title:1, year:1})

// Title of PG-13 (rated) movies that have won at least 3 awards
db.movies.find({$and:[{rated: "PG-13"},{"awards.wins": {$gte: 3}}]}, {_id:0, title:1, rated:1, "awards.wins": 1})

/*
sample_restaurants : restaurants
    • Name of all restaurants in Brooklyn (borough)
    • Name and borough of all American cuisine restaurants in Queens (borough)

*/

// Name of all restaurants in Brooklyn (borough)
db.restaurants.find({borough: "Brooklyn"},{_id:0, name: 1, borough:1})

// Name and borough of all American cuisine restaurants in Queens (borough)
db.restaurants.find({$and:[{cuisine: "American"},{borough: "Queens"}]}, {_id:0, name:1, borough:1})

