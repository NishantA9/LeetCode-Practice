-- SQL Lesson 2: Queries with constraints 

-- Operator	Condition	SQL Example
-- =, !=, <, <=, >, >=	Standard numerical operators	col_name != 4
-- BETWEEN … AND …	Number is within range of two values (inclusive)	col_name BETWEEN 1.5 AND 10.5
-- NOT BETWEEN … AND …	Number is not within range of two values (inclusive)	col_name NOT BETWEEN 1 AND 10
-- IN (…)	Number exists in a list	col_name IN (2, 4, 6)
-- NOT IN (…)	Number does not exist in a list	col_name NOT IN (1, 3, 5)

-- Exercise 2 — Tasks
-- Find the movie with a row id of 6
SELECT id, title FROM movies where id = 6;

-- Find the movies released in the years between 2000 and 2010
SELECT * FROM movies where Year BETWEEN 2000 AND 2010;

-- Find the movies not released in the years between 2000 and 2010
SELECT * FROM movies where Year not BETWEEN 2000 AND 2010;

-- Find the first 5 Pixar movies and their release year
SELECT * FROM movies where Year < 2004;
--another solution
SELECT title, year FROM movies WHERE year <= 2003;