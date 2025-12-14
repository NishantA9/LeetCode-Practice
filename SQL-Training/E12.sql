-- SQL Lesson 12: Order of execution of a Query
-- Exercise 12 — Tasks
-- Find the number of movies each director has directed
SELECT director, COUNT(id) as Num_movies_directed FROM movies GROUP BY director;

-- Find the total domestic and international sales that can be attributed to each director
select director, Sum(domestic_sales + international_sales) as totalSale from Movies inner join boxoffice on movie_id = id group by director;