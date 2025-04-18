from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}  # Step 1: Create adjacency list from tickets
        tickets.sort() # Step 2: Sort tickets to ensure lexical order traversal
        for src, dst in tickets: # Step 3: Fill adjacency list after sorting
            adj[src].append(dst)
        res = ["JFK"]  # Initialize the result path with the starting point
        def dfs(src):  # Step 4: Backtracking DFS
            if len(res) == len(tickets) + 1:  # If result has all tickets used, we've found a valid path
                return True
            if src not in adj: # If no flights from this source, return False
                return False
            temp = list(adj[src]) # Try all destinations from current source, Clone the list to iterate safely
            for i, v in enumerate(temp):
                adj[src].pop(i) # Remove the destination from the graph (simulate using the ticket)
                res.append(v)
                if dfs(v):  #Recursively try next airport
                    return True
                adj[src].insert(i, v) # Backtrack: undo the move
                res.pop()
            return False
        dfs("JFK") # Step 5: Start DFS from "JFK"
        return res
    
    
# -----------------------------------------------------------------
# Alternative Solutions
# Example usage
# 2. Hierholzer's Algorithm (Recursion)
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         adj = defaultdict(list)
#         for src, dst in sorted(tickets)[::-1]:
#             adj[src].append(dst)
#         res = []
#         def dfs(src):
#             while adj[src]:
#                 dst = adj[src].pop()
#                 dfs(dst)
#             res.append(src)
#         dfs('JFK')
#         return res[::-1]