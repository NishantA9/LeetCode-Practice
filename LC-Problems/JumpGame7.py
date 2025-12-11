from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])  # BFS queue starting from index 0
        farthest = 0  # furthest index we've already enqueued
        while q:
            i = q.popleft()  # current position
            start = max(i + minJump, farthest + 1)  # avoid rechecking indices <= farthest
            for j in range(start, min(i + maxJump + 1, len(s))):  # explore reachable window
                if s[j] == "0":  # can land only on '0'
                    q.append(j)  # enqueue reachable index
                    if j == len(s) - 1:  # reached end
                        return True
            farthest = i + maxJump  # update farthest we have considered from this i
        return False  # couldn't reach the end