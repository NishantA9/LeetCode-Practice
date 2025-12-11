from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort first to handle duplicates easily
        def dfs(i, cur, total):
            if total == target: # Base Case: If total equals target, save the combination
                res.append(cur.copy())
                return
            if total > target or i == len(candidates): # If we exceed the target or reach the end of the list
                return
            cur.append(candidates[i])   # Include candidates[i] in the combination
            dfs(i + 1, cur, total + candidates[i])  # Move to next index (no reuse)
            cur.pop()  # Backtrack
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: # Skip duplicate numbers to avoid repeated combinations
                i += 1
            dfs(i + 1, cur, total) # Don't include candidates[i]
        dfs(0, [], 0)
        return res