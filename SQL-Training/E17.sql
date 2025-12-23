-- SQL Lesson 17: Altering tables Exercise 17 — Tasks
-- Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in.
ALTER TABLE movies ADD Aspect_Ratio float;

-- Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.
ALTER TABLE movies ADD Language TEXT DEFAULT 'English';