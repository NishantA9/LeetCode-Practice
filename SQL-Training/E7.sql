-- Exercise 7 — Tasks SQL Lesson 7: OUTER JOINs
-- Find the list of all buildings that have employees
SELECT DISTINCT building FROM employees;
-- I messed up in above query where I wrote the below query instead of above
SELECT * FROM employees Join buildings on employees.BUILDING = buildings.building_name not null;

-- Find the list of all buildings and their capacity 
SELECT * from buildings;
-- same here I wrote this below query instead of above, I was focused on writing left join but the tables were easy to write
SELECT building, capacity FROM employees left join buildings on employees.BUILDING = buildings.building_name;

-- List all buildings and the distinct employee roles in each building (including empty buildings) (was not able to solve it as I need to check solution)
SELECT DISTINCT building_name, role FROM buildings LEFT JOIN employeesON building_name = building;