from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)} # Map each course to a list of prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visitSet = set()  # Tracks courses in the current DFS path
        def dfs(crs):
            if crs in visitSet:
                return False  # Cycle detected
            if preMap[crs] == []:
                return True  # Already processed
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []  # Mark course as completed
            return True
        for crs in range(numCourses): # Check each course
            if not dfs(crs):
                return False
        return True