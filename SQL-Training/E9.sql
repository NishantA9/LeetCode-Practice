-- SQL Lesson 9: Queries with expressions, Exercise 9 — Tasks
-- List all movies and their combined sales in millions of dollars
select * from Movies inner join Boxoffice on Movies.id = movie_id where  domestic_sales + international_sales as combinedSales;
-- the above query is incorrect, correct version below
Select Title, (domestic_sales+international_sales)/1000000 as CombinedSales from Movies join boxoffice on movies.id = boxoffice.movie_id;

-- List all movies and their ratings in percent
Select Title, rating*10 as ratingpercent from Movies join boxoffice on movies.id = boxoffice.movie_id;

-- List all movies that were released on even number years
Select Title, (Year/2) as EvenYear from Movies join boxoffice on movies.id = boxoffice.movie_id;
-- the above query is incorrect, correct version below
SELECT title, year FROM movies WHERE year % 2 = 0;