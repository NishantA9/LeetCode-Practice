-- SQL Lesson 10: Queries with aggregates (Pt. 1)
-- Here are some common aggregate functions that we are going to use in our examples:

-- Function	Description
-- COUNT(*), COUNT(column)	A common function used to counts the number of rows in the group if no column name is specified. Otherwise, count the number of rows in the group with non-NULL values in the specified column.
-- MIN(column)	Finds the smallest numerical value in the specified column for all rows in the group.
-- MAX(column)	Finds the largest numerical value in the specified column for all rows in the group.
-- AVG(column)	Finds the average numerical value in the specified column for all rows in the group.
-- SUM(column)	Finds the sum of all numerical values in the specified column for the rows in the group.
-- Docs: MySQL, Postgres, SQLite, Microsoft SQL Server

-- SQL Lesson 10: Queries with aggregates (Pt. 1) Exercise 10 — Tasks
-- Find the longest time that an employee has been at the studio
select max(years_employed) from employees;

-- For each role, find the average number of years employed by employees in that role
select role, avg(years_employed) from employees group by role;

-- Find the total number of employee years worked in each building
select building, sum(years_employed) from employees group by building;    
