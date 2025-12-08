
-- Link to Practice - https://sqlbolt.com/lesson/select_queries_introduction
-- We will be using a database with data about some of Pixar's classic movies for most of our exercises. 
-- This first exercise will only involve the Movies table, and the default query below currently shows all the properties of 
-- each movie. To continue onto the next lesson, alter the query to find the exact information we need for each task. 

--EX1 Select

-- Q1 - Find the title of each film
SELECT title FROM movies;

-- Q2 - Find the director of each film
SELECT director FROM movies;

-- Q3 -  Find the title and director of each film
SELECT title, director FROM movies;

-- Q4 -  Find the title and year of each film
SELECT title, year FROM movies;

-- Q5 - Find all the information about each film
SELECT * FROM movies;
