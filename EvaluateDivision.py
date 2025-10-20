from typing import List
import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)  # Build graph: node -> [(neighbor, division_result)]
        for i, eq in enumerate(equations):  # Process each equation a/b = value
            a, b = eq
            adj[a].append((b, values[i]))  # Add edge a->b with weight a/b
            adj[b].append((a, 1 / values[i]))  # Add reverse edge b->a with weight b/a (reciprocal)
        def dfs(src: str, target: str, visited: set) -> float:  # DFS to find path product from src to target
            if src not in adj or target not in adj:  # Invalid if either variable not in graph
                return -1
            if src == target:  # Found target, product is 1 (x/x = 1)
                return 1
            visited.add(src)  # Mark current node as visited
            for nei, weight in adj[src]:  # Check all neighbors
                if nei not in visited:  # Skip visited nodes to avoid cycles
                    result = dfs(nei, target, visited)  # Recursively find path to target
                    if result != -1:  # Found valid path, multiply edges
                        return weight * result
            return -1  # No valid path found
        return [dfs(q[0], q[1], set()) for q in queries]  # Process each query using DFS