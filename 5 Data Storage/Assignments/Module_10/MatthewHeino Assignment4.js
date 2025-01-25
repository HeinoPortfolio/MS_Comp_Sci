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
 db.grades.find({$and:[{class_id: 149}, {scores:{$elemMatch:{type:"quiz", score: {$lt: 10}}}}]},
 {_id:0, student_id: 1, class_id:1,scores:{$slice:[1,1]}}) 
 
 
 /*
 sample_training : zips
 
    • State IN
    • State IN or CA
    • State IN and zip 47304
*/

