from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Handle single node case
        if n == 1:  # If only one node, it must be the root
            return [0]         
        # Build undirected graph as adjacency list
        adj = [[] for _ in range(n)]  # Initialize empty adjacency list
        for u, v in edges:  # Add edges in both directions
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node: int, parent: int) -> int:  # Returns height of tree rooted at node
            hgt = 0  # Current height of subtree
            for nei in adj[node]:  # Check all neighbors
                if nei == parent:  # Skip parent to avoid cycles
                    continue
                hgt = max(hgt, 1 + dfs(nei, node))  # Height is max of all subtrees + 1
            return hgt
        minHgt = n  # Start with maximum possible height
        res = []  # Store nodes that give minimum height
        for i in range(n):  # Try each node as root
            curHgt = dfs(i, -1)  # Get height with current node as root
            if curHgt == minHgt:  # If same as current min, add to result
                res.append(i)
            elif curHgt < minHgt:  # If better than current min, start new result
                res = [i]
                minHgt = curHgt
        return res