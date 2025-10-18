from typing import List
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:         # If starting position is a deadend, impossible to reach target
        if "0000" in deadends:
            return -1
        def children(lock: str) -> List[str]:
            """Generate all possible combinations by rotating one digit up or down."""
            res = []
            for i in range(4):  # For each digit position
                digit = str((int(lock[i]) + 1) % 10)                 # Rotate digit up (0->1, 1->2, ..., 9->0)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)                 # Rotate digit down (0->9, 1->0, ..., 9->8)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        q = deque([("0000", 0)])         # BFS queue: (lock combination, number of turns) Start from "0000" with 0 turns
        visit = set(deadends)        # Use deadends as initial visited set to avoid these combinations
        while q:          # BFS to find shortest path to target
            lock, turns = q.popleft()
            if lock == target:         # Found target combination
                return turns
            for child in children(lock):
                if child not in visit:                 # Only explore unvisited combinations
                    visit.add(child)
                    q.append((child, turns + 1))
        return -1       # No valid path to target found