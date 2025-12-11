--SQL Lesson 3: Queries with constraints (Pt. 2)

-- Operator	Condition	Example
-- =	Case sensitive exact string comparison (notice the single equals)	col_name = "abc" 
-- : != or <>	Case sensitive exact string inequality comparison	col_name != "abcd"
-- LIKE	Case insensitive exact string comparison	col_name LIKE "ABC"
-- NOT LIKE	Case insensitive exact string inequality comparison	col_name NOT LIKE "ABCD"
-- %	Used anywhere in a string to match a sequence of zero or more characters (only with LIKE or NOT LIKE)	col_name LIKE "%AT%"
-- (matches "AT", "ATTIC", "CAT" or even "BATS")
-- _	Used anywhere in a string to match a single character (only with LIKE or NOT LIKE)	col_name LIKE "AN_"
-- (matches "AND", but not "AN")
-- IN (…)	String exists in a list	col_name IN ("A", "B", "C")
-- NOT IN (…)	String does not exist in a list	col_name NOT IN ("D", "E", "F")

-- Exercise 3 — Tasks
-- Find all the Toy Story movies 
SELECT * FROM movies WHERE Title LIKE "%Toy%";

-- Find all the movies directed by John Lasseter
SELECT * FROM movies WHERE director = "John Lasseter"; 
--or
SELECT * FROM movies WHERE director LIKE "%John%";

-- Find all the movies (and director) not directed by John Lasseter
SELECT * FROM movies WHERE director != "John Lasseter";

-- Find all the WALL-* movies
SELECT * FROM movies WHERE Title LIKE "%WALL%";