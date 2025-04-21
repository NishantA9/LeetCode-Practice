from typing import List
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}        # Step 1: Build the adjacency list for all unique characters
        for i in range(len(words) - 1):        # Step 2: Compare adjacent words to find the order
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:             # Invalid case: longer word comes before its prefix
                return ""
            for j in range(minLen):            # Find the first different character and create a directed edge
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}  # False = visited, True = visiting (current path) // Step 3: Topological Sort using DFS
        res = [] 
        def dfs(c):
            if c in visit:
                return visit[c]  # If visiting -> cycle detected
            visit[c] = True  # Mark node as visiting
            for nei in adj[c]:
                if dfs(nei):
                    return True  # Cycle detected
            visit[c] = False  # Mark node as fully visited
            res.append(c)  # Add to result after visiting all neighbors
        for c in adj:        # Step 4: Visit all nodes
            if dfs(c):
                return ""  # Cycle detected → invalid order
        res.reverse()  # Reverse to get correct order
        return "".join(res)