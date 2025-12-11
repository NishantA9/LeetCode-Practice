from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []   # Result list to store all unique permutations
        perm = []  # Current permutation being built  
        count = {n: 0 for n in nums} # Count frequency of each number to handle duplicates
        for num in nums:
            count[num] += 1
        def dfs():  # Depth-first search to generate permutations
            if len(perm) == len(nums):  # Base case: permutation is complete
                res.append(perm.copy())  # Add copy of current permutation
                return
            for num in count:             # Try each unique number that still has available count
                if count[num] > 0:  # If this number is still available
                    perm.append(num)    # Add number to current permutation
                    count[num] -= 1     # Decrease available count
                    dfs()               # Recursively build rest of permutation
                    count[num] += 1     # Backtrack: restore count
                    perm.pop()          # Backtrack: remove number from permutation
        dfs()      # Start the DFS
        return res # Return all unique permutations