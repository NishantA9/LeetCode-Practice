from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []         # Final result to store all subsets
        subset = []      # Current subset being built
        def dfs(i):
            if i >= len(nums): # Base Case: reached end of list
                res.append(subset.copy())  # Add a copy of current subset
                return
            subset.append(nums[i])# Decision to include nums[i]
            dfs(i + 1)
            subset.pop()# Backtrack: remove nums[i] and explore path without it
            dfs(i + 1)
        dfs(0)  # Start from index 0
        return res