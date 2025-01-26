/* 
	Matthew Heino
	DSCI 604 Data Management and Storage
	Assignment #4 from Module 10
	Due Date: March 25, 2025
	
*/

/*
sampe_training : grades

    • class_id 339
    • exam scores greater than 90
    • quiz scores less than 60 and class_id 149 

*/

// class_id 339
db.grades.find({class_id: 339})

// exam scores greater than 90
db.grades.find({scores: {$elemMatch:{type:"exam", score: {$gt: 90}}}}, {_id:0, scores:{$slice: 1}})

// quiz scores less than 60 and class_id 149 
 db.grades.find({$and:[{class_id: 149}, {scores:{$elemMatch:{type:"quiz", score: {$lt: 60}}}}]},
 {_id:0, student_id: 1, class_id:1,scores:{$slice:[1,1]}}) 
 
 
 /*
 sample_training : zips
 
    • State IN
    • State IN or CA
    • State IN and zip 47304
*/

// State IN
db.zips.find({state: 'IN'})

// State IN or CA
db.zips.find({$or: [{state: 'IN'}, {state:'CA'}]})

// State IN and zip 47304
db.zips.find({$and: [{state: 'IN'}, {zip:'47304'}]})

/*
sample_training : companies
    • founded_year greater than 2010
    • category_code news or music
    • founded year greater than 2007 and number of employees greater than 100
*/

// founded_year greater than 2010
db.companies.find({founded_year:{$gt: 2010}})

//category_code news or musi
db.companies.find({category_code: {$in: ["news","music"]}})

// founded year greater than 2007 and number of employees greater than 100
db.companies.find({$and: [{founded_year: {$gt: 2007}}, {number_of_employees: {$gt: 100}}]})

/*
sample_training : routes
    • All routes from DTW to TPA
    • All United Airlines routes (iata is UAL)
*/
// All routes from DTW to TPA
db.routes.find({$and: [{src_airport: "DTW"}, {dst_airport: "TPA"}]})

// All United Airlines routes (iata is UAL)
db.routes.find({"airline.iata": 'UAL'})

/*
sample_mflix : theaters
    • Theaters located in the state of MD
*/

// Theaters located in the state of MD
db.theaters.find({"location.address.state": "MD"})







