from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]  # Parent array (1-based indexing)
        rank = [1] * (N + 1)             # Rank (used for balancing trees)
        def find(n):        # Find with path compression
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        def union(n1, n2):        # Union with rank
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False  # Cycle detected
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        for n1, n2 in edges: # Go through all edges, return the one that forms a cycle
            if not union(n1, n2):
                return [n1, n2]