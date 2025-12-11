from collections import deque
from typing import List
class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()          # Track visited cells
        q = deque()            # Queue for BFS
        # Helper to add valid neighboring rooms to queue
        def addRoom(r, c):
            if (r < 0 or r == ROWS or 
                c < 0 or c == COLS or 
                (r, c) in visit or 
                rooms[r][c] == -1):  # Wall
                return
            visit.add((r, c))
            q.append([r, c])
        # Step 1: Add all gates to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:  # Gate
                    q.append([r, c])
                    visit.add((r, c))
        # Step 2: BFS from all gates
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist   # Update distance
                # Explore neighbors
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1  # Increase distance after each level