from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]  # Initially, each node is its own parent
        rank = [1] * n               # Rank (or size) of each component
        def find(n1):        # Find function with path compression
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]  # Path compression
                res = par[res]
            return res
        def union(n1, n2):        # Union by rank: merge two components if they have different roots
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0  # Already connected
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p1] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n  # Start with n components
        for n1, n2 in edges:
            res -= union(n1, n2)  # Reduce count if a union was successful
        return res