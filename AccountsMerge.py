from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailIdx = {}  # Maps email to its unique index for graph representation
        emails = []  # List of all unique emails (index matches emailIdx)
        emailToAcc = {}  # Maps email index to its original account ID
        # First pass: Assign unique indices to each email
        m = 0  # Counter for unique email indices
        for accId, a in enumerate(accounts):  # For each account
            for i in range(1, len(a)):  # Skip name (index 0), process emails
                email = a[i]
                if email in emailIdx:  # Skip if email already indexed
                    continue
                emails.append(email)  # Store email
                emailIdx[email] = m  # Map email to its index
                emailToAcc[m] = accId  # Remember which account this email belongs to
                m += 1
        # Build adjacency list: connect emails belonging to same account
        adj = [[] for _ in range(m)]  # Graph as adjacency list
        for a in accounts:  # For each account
            for i in range(2, len(a)):  # Connect consecutive emails
                id1 = emailIdx[a[i]]  # Current email index
                id2 = emailIdx[a[i - 1]]  # Previous email index
                adj[id1].append(id2)  # Add bidirectional edges
                adj[id2].append(id1)
        emailGroup = defaultdict(list)  # Groups emails by account after merging
        visited = [False] * m  # Track visited emails in DFS
        def dfs(node: int, accId: int) -> None:  # DFS to collect connected emails
            visited[node] = True  # Mark as visited
            emailGroup[accId].append(emails[node])  # Add email to its group
            for nei in adj[node]:  # Visit all connected emails
                if not visited[nei]:
                    dfs(nei, accId)
        # Find connected components (merged accounts)
        for i in range(m):  # Process each email
            if not visited[i]:  # Start DFS from unvisited emails
                dfs(i, emailToAcc[i])  # Group emails connected to this one
        # Build final result
        res = []
        for accId in emailGroup:  # For each merged account group
            name = accounts[accId][0]  # Get account owner's name
            res.append([name] + sorted(emailGroup[accId]))  # Add name and sorted emails
        return res