from typing import List
from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)  # Map each course to its prerequisites
        for prereq, crs in prerequisites:  # Build adjacency list: course -> list of prerequisites
            adj[crs].append(prereq)            
        def dfs(crs: int) -> set:  # Returns set of all prerequisites (direct and indirect) for a course
            if crs not in prereqMap:  # If not computed yet, find all prerequisites recursively
                prereqMap[crs] = set()  # Initialize empty set for current course
                for prereq in adj[crs]:  # Get prerequisites of prerequisites
                    prereqMap[crs] |= dfs(prereq)  # Union with prerequisites of current prerequisite
                prereqMap[crs].add(crs)  # Add current course to its prerequisite set
            return prereqMap[crs]  # Return cached result            
        prereqMap = {}  # Maps each course to set of all its prerequisites
        for crs in range(numCourses):  # Process all courses
            dfs(crs)  # Build prerequisite map for each course            
        res = []  # Store query results
        for u, v in queries:  # Check if u is a prerequisite of v
            res.append(u in prereqMap[v])  # True if u is in v's prerequisite set
        return res