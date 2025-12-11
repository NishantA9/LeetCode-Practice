# from typing import List
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         # Handle single node case
#         if n == 1:  # If only one node, it must be the root
#             return [0]         
#         # Build undirected graph as adjacency list
#         adj = [[] for _ in range(n)]  # Initialize empty adjacency list
#         for u, v in edges:  # Add edges in both directions
#             adj[u].append(v)
#             adj[v].append(u)
#         def dfs(node: int, parent: int) -> int:  # Returns height of tree rooted at node
#             hgt = 0  # Current height of subtree
#             for nei in adj[node]:  # Check all neighbors
#                 if nei == parent:  # Skip parent to avoid cycles
#                     continue
#                 hgt = max(hgt, 1 + dfs(nei, node))  # Height is max of all subtrees + 1
#             return hgt
#         minHgt = n  # Start with maximum possible height
#         res = []  # Store nodes that give minimum height
#         for i in range(n):  # Try each node as root
#             curHgt = dfs(i, -1)  # Get height with current node as root
#             if curHgt == minHgt:  # If same as current min, add to result
#                 res.append(i)
#             elif curHgt < minHgt:  # If better than current min, start new result
#                 res = [i]
#                 minHgt = curHgt
#         return res


#topological sort / BFS approach
from typing import List
from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:  # Single node case: the node is the only centroid
            return [0]
       # Build undirected graph using adjacency lists
        adj = defaultdict(list)  # node -> list of neighbors
        for n1, n2 in edges:  # Create edges in both directions
            adj[n1].append(n2)
            adj[n2].append(n1)
        # Track degree (number of edges) for each node
        edge_cnt = {}  # node -> number of remaining edges
        leaves = deque()  # Queue to process leaf nodes (degree = 1)
        # Initialize degrees and find initial leaves
        for src, neighbors in adj.items():  # For each node
            edge_cnt[src] = len(neighbors)  # Count its edges
            if len(neighbors) == 1:  # If it's a leaf
                leaves.append(src)  # Add to processing queue
        # Remove leaves layer by layer until we reach centroids
        while leaves:  # Process leaves until we find centroids
            if n <= 2:  # When 1 or 2 nodes remain, they are centroids
                return list(leaves)              
            # Remove current layer of leaves
            for _ in range(len(leaves)):  # Process current layer
                node = leaves.popleft()  # Remove leaf node
                n -= 1  # Decrease remaining nodes count
                for nei in adj[node]:  # Update neighbors
                    edge_cnt[nei] -= 1  # Remove edge to this leaf
                    if edge_cnt[nei] == 1:  # If neighbor becomes leaf
                        leaves.append(nei)  # Process in next layer
                        
 #Dynamic Programming On Trees (Rerooting) works on LC                     
class Solution3:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp = [[0] * 2 for _ in range(n)] # top two heights for each node
        def dfs(node, parent):
            for nei in adj[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
                curHgt = 1 + dp[nei][0]
                if curHgt > dp[node][0]:
                    dp[node][1] = dp[node][0]
                    dp[node][0] = curHgt
                elif curHgt > dp[node][1]:
                    dp[node][1] = curHgt
        def dfs1(node, parent, topHgt):
            if topHgt > dp[node][0]:
                dp[node][1] = dp[node][0]
                dp[node][0] = topHgt
            elif topHgt > dp[node][1]:
                dp[node][1] = topHgt
            for nei in adj[node]:
                if nei == parent:
                    continue
                toChild = 1 + (dp[node][1] if dp[node][0] == 1 + dp[nei][0] else dp[node][0])
                dfs1(nei, node, toChild)
        dfs(0, -1)
        dfs1(0, -1, 0)
        minHgt, res = n, []
        for i in range(n):
            minHgt = min(minHgt, dp[i][0])
        for i in range(n):
            if minHgt == dp[i][0]:
                res.append(i)
        return res                               