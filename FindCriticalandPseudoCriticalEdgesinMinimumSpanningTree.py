from typing import List
class UnionFind:  # Union-Find data structure for Kruskal's algorithm
    def __init__(self, n):
        self.par = [i for i in range(n)]  # Each node is its own parent initially
        self.rank = [1] * n  # Track size of each component for union by rank

    def find(self, v1):  # Find parent with path compression
        while v1 != self.par[v1]:  # Follow parent pointers until root
            self.par[v1] = self.par[self.par[v1]]  # Path compression
            v1 = self.par[v1]
        return v1

    def union(self, v1, v2):  # Union by rank
        p1, p2 = self.find(v1), self.find(v2)  # Find parents
        if p1 == p2:  # Already in same component
            return False
        if self.rank[p1] > self.rank[p2]:  # Merge smaller into larger
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):  # Add original indices to edges
            e.append(i)  # [v1, v2, weight, original_index]
        edges.sort(key=lambda e: e[2])  # Sort edges by weight for Kruskal's
        mst_weight = 0  # Weight of the minimum spanning tree
        uf = UnionFind(n)  # Build the MST to get its weight
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):  # Add edge if it doesn't create cycle
                mst_weight += w

        critical, pseudo = [], []  # Store critical and pseudo-critical edges
        for n1, n2, e_weight, i in edges:  # Test each edge
            # Try building MST without current edge
            weight = 0
            uf = UnionFind(n)
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):  # Skip current edge
                    weight += w
            if max(uf.rank) != n or weight > mst_weight:  # Edge is critical if MST impossible or heavier
                critical.append(i)
                continue

            # Try building MST with current edge forced
            uf = UnionFind(n)
            uf.union(n1, n2)  # Force include current edge
            weight = e_weight
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):  # Add other edges
                    weight += w
            if weight == mst_weight:  # Edge is pseudo-critical if MST weight unchanged
                pseudo.append(i)
        return [critical, pseudo]