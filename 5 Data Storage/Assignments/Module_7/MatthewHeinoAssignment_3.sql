/* 		Matthew Heino
		Course: DSCI 604 Data Storage
        Assignment # 3
        Due Date: February 23, 2025
*/
use world;

-- 1) List Names of all countries in the Continent of North America
SELECT country.Name FROM Country
WHERE Continent ='North America';

-- 2) List Name, Continent, and Region for all countries whose Surface Area is more than or equal to 1,000,000
SELECT country.Name, Continent, Region FROM country
WHERE SurfaceArea >= 1000000;

-- 3) List Names of all countries whose GovernmentForm is Constitutional Monarchy
SELECT country.Name FROM country
WHERE GovernmentForm = 'Constitutional Monarchy';

-- 4) List country Names and their Capital (name) for all countries in the Continent of South America
SELECT co.Name AS 'Country Name' , ci.Name AS 'Capital Name'
FROM country co
INNER JOIN city ci ON co.Capital = ci.ID
WHERE co.Continent = 'South America';

-- 5) List all fields for countries whose Population is more than 500,000,000
SELECT * 
FROM country
WHERE Population > 500000000; 

-- 6) List all fields for counties whose GovernmentForm is Federal Republic
SELECT * 
FROM country
WHERE GovernmentForm = 'Federal Republic';

-- 7) List sum of Population of each Continent (grouped by Continent)
SELECT Continent,  SUM(Population) AS 'Continental Population'
FROM country
GROUP BY Continent;

-- 8) List Names of counties whose Language is German
SELECT co.Name AS 'Country Name' 
FROM country co
INNER JOIN countrylanguage  cl ON co.Code = cl.CountryCode 
WHERE cl.Language = 'German';

-- 9) List all fields for countries whose Population is more than or equal 
-- to 200,000,000 and whose Surface Area is more than or equal to 500,000
SELECT * 
FROM country
WHERE Population >= 200000000
AND SurfaceArea >= 500000;

-- 10 List Names of countries whose Independence Year is NULL
SELECT * FROM country
WHERE IndepYear IS NULL;

-- 11) List Names of all cities in the United Kingdom
SELECT city.name 
FROM city
WHERE city.CountryCode = 
	(
		SELECT country.Code 
		FROM country 
		WHERE country.Name = 'United Kingdom' 
	);

-- 12) List Names of all cities in the State (field name in the table is District) of Texas in the United States of America
SELECT city.Name 
FROM city
WHERE District = 'Texas';

-- 13) List all fields for countries whose LifeExpectancy is between 50% and 70% (inclusive)
SELECT * 
FROM country
WHERE LifeExpectancy >= 50 AND LifeExpectancy <= 70;