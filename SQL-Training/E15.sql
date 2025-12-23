-- SQL Lesson 15: Deleting rows, Exercise 15 — Tasks
-- This database is getting too big, lets remove all movies that were released before 2005.
Delete FROM movies where Year < 2005;

-- Andrew Stanton has also left the studio, so please remove all movies directed by him.
Delete FROM movies where Director = 'Andrew Stanton';