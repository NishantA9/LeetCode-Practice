from typing import List
class UnionFind:
    def __init__(self, n):
        self.n = n  # Number of disjoint sets
        self.Parent = list(range(n + 1))  # Parent array for union-find
        self.Size = [1] * (n + 1)  # Size of each set for union by size
        
    def find(self, node):
        if self.Parent[node] != node: # Find root with path compression
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        # Find roots of both nodes
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:  # Already in same set
            return False
        self.n -= 1  # Decrease count of disjoint sets
        # Union by size: attach smaller tree under root of larger tree
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]  # Update size
        self.Parent[pv] = pu  # Merge sets
        return True

    def isConnected(self):
        return self.n == 1  # Check if all nodes are in one set

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums)) # Initialize UnionFind with size of nums
        factor_index = {}  # Maps prime factor to first index where it appears
        
        for i, n in enumerate(nums):
            f = 2  # Start checking from smallest prime factor
            # Find all prime factors up to sqrt(n)
            while f * f <= n:
                if n % f == 0:  # If f is a factor
                    if f in factor_index:  # Connect with previous number with same factor
                        uf.union(i, factor_index[f])
                    else:  # First occurrence of this factor
                        factor_index[f] = i
                    # Remove all occurrences of this prime factor
                    while n % f == 0:
                        n = n // f
                f += 1
            # Handle remaining prime factor if exists
            if n > 1:  # n is prime itself
                if n in factor_index:
                    uf.union(i, factor_index[n])
                else:
                    factor_index[n] = i
        return uf.isConnected()  # True if all numbers are connected