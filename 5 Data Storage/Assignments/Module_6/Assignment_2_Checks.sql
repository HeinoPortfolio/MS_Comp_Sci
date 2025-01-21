-- Check question number 1
SELECT * FROM customer WHERE last_name = 'Doe';

-- Check question #2 
SELECT * FROM film WHERE film.description = 'A movie about the world of coding.';

-- Check question #3
SELECT * FROM actor WHERE  first_name = 'Emily' AND last_name ='Blunt';

-- Check Question 5
SELECT * FROM film WHERE film_id = 732;


SELECT film.description FROM film;

SELECT rental_rate FROM film 
WHERE rental_rate < 2.00;

# Check question # 8 
SELECT * FROM film
WHERE title = 'Code Masters';

# Check question #9
SELECT rental_date
FROM rental;


# Check question #11
SELECT DISTINCT(customer_id) 
FROM rental;

SELECT *  
FROM category;

select * FROM category;

SELECT * FROM film_category;
SELECT film.film_id AS "Film ID", film_category.film_id AS "FC Film ID", film_category.category_id, category.name AS "Cateogory Name"
FROM film
INNER JOIN film_category
ON film_category.film_id = film.film_id
INNER JOIN category
ON category.category_id = film_category.category_id
GROUP BY category.name;


SELECT SUM(amount) AS "Total Revenue", payment.staff_id AS "Payment staff ID",
		staff.staff_id AS "STAFF staff_id", store_id
FROM payment
INNER JOIN staff
ON staff.staff_id = payment.staff_id
GROUP BY staff.store_id;



