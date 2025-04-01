from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]  # Base case: one empty permutation when input is empty
        perms = self.permute(nums[1:])  # Recursively get permutations of remaining list
        res = []
        for p in perms:
            # Insert the first element (nums[0]) at every possible position in each permutation
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, nums[0])
                res.append(pCopy)
        return res