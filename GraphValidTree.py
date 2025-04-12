from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True  # Empty graph is technically a valid tree
        adj = {i: [] for i in range(n)}        # Build adjacency list for the graph
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        def dfs(i, prev):        # DFS to detect cycles and check connectivity
            if i in visit:
                return False  # Cycle detected
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue  # Don't go back to the parent node
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, -1) and n == len(visit) # Check if the graph is connected and has no cycles