from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []  # To store all valid combinations
        def dfs(i, cur, total):
            if total == target: # Base case: if total == target, add the current combo to result
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target: # If out of bounds or total exceeded target, stop this path
                return
            cur.append(nums[i]) # Choose the current number (we can reuse it)
            dfs(i, cur, total + nums[i])  # stay at i to reuse
            cur.pop()  # backtrack
            dfs(i + 1, cur, total)  # Skip current number and move to next
        dfs(0, [], 0)  # Start DFS with index 0, empty path, and total = 0
        return res