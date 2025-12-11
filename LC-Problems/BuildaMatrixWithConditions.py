from collections import defaultdict
from typing import List
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # DFS helper to detect cycles and build topological order
        def dfs(src, adj, visit, path, order):
            if src in path:  # Found a cycle
                return False
            if src in visit:  # Already processed this node
                return True
            visit.add(src)  # Mark as visited
            path.add(src)  # Add to current path
            for nei in adj[src]:  # Check all neighbors
                if not dfs(nei, adj, visit, path, order):
                    return False
            path.remove(src)  # Remove from path after processing
            order.append(src)  # Add to final order
            return True

        # Create topological sort for given edges
        def topo_sort(edges):
            adj = defaultdict(list)  # Create adjacency list
            for src, dst in edges:
                adj[src].append(dst)

            visit, path = set(), set()  # Track visited nodes and current path
            order = []
            for src in range(1, k + 1):  # Process all nodes
                if src not in visit:
                    if not dfs(src, adj, visit, path, order):
                        return []  # Return empty if cycle found
            return order[::-1]  # Reverse for correct order

        # Get row ordering based on conditions
        row_order = topo_sort(rowConditions)
        if not row_order:
            return []  # Return empty if no valid row order

        # Get column ordering based on conditions
        col_order = topo_sort(colConditions)
        if not col_order:
            return []  # Return empty if no valid column order

        # Map values to their positions in row and column order
        val_to_row = {num: i for i, num in enumerate(row_order)}
        val_to_col = {num: i for i, num in enumerate(col_order)}
        
        # Create empty matrix
        res = [[0] * k for _ in range(k)]
        
        # Fill matrix based on row and column positions
        for num in range(1, k + 1):
            r, c = val_to_row[num], val_to_col[num]
            res[r][c] = num

        return res