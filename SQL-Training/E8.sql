-- SQL Lesson 8: A short note on NULLs Exercise 8 — Tasks
-- Find the name and role of all employees who have not been assigned to a building ✓
SELECT Name, Role FROM employees WHERE building Is Null ;

-- Find the names of the buildings that hold no employees
Select Distinct Building_name from Buildings Left Join employees on buildings.building_name = employees.building where Role is Null;