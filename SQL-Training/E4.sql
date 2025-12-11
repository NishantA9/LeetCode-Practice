-- SQL Lesson 4: Filtering and sorting Query results
-- Exercise 4 — Tasks
-- List all directors of Pixar movies (alphabetically), without duplicates
SELECT Distinct Director FROM movies Order by director ASC;

-- List the last four Pixar movies released (ordered from most recent to least)
SELECT * FROM movies Order by Year desc LIMIT 4;

-- List the first five Pixar movies sorted alphabetically
SELECT * FROM movies Order by Title ASC LIMIT 5;

-- List the next five Pixar movies sorted alphabetically
SELECT * FROM movies Order by Title ASC LIMIT 5 offset 5;