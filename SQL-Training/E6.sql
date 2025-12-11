-- Exercise 6 — Tasks SQL Lesson 6: Multi-table queries with JOINs
-- Find the domestic and international sales for each movie
SELECT * FROM movies join boxoffice on movies.id = boxoffice.movie_id;

-- Show the sales numbers for each movie that did better internationally rather than domestically
SELECT * FROM movies inner join boxoffice on movies.id = boxoffice.movie_id where international_sales > domestic_sales;

-- List all the movies by their ratings in descending order
SELECT * FROM movies inner join boxoffice on movies.id = boxoffice.movie_id order by rating desc;