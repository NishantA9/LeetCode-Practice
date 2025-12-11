from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}        # Step 1: Build graph
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        output = []    # List to hold the topological order
        visit = set()  # Courses that are fully processed
        cycle = set()  # Courses in current DFS path (to detect cycles)
        def dfs(crs):
            if crs in cycle:
                return False  # Cycle detected
            if crs in visit:
                return True   # Already processed
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)  # Post-order add
            return True
        for c in range(numCourses): # Step 2: Visit all courses
            if not dfs(c):
                return []  # If cycle detected, return []
        return output  # Already in correct order due to post-order logic