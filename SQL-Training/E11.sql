-- SQL Lesson 11: Queries with aggregates (Pt. 2)
-- Exercise 11 — Tasks
-- Find the number of Artists in the studio (without a HAVING clause) use COUNT(*) instead of Role  as its safer if role could be NULL
SELECT Count(Role) as No_Artist from Employees where Role = 'Artist';

-- Find the number of Employees of each role in the studio
SELECT Role, Count(Role) as No_Artist from Employees Group By Role;

-- Find the total number of years employed by all Engineers
Select sum(years_employed) as TotalNoOfYears from Employees where Role = 'Engineer';