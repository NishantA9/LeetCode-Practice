from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0  # Initialize result to store OR of all elements   
        for num in nums: # Calculate bitwise OR of all elements in the array
            res |= num  # OR current number with result
        # Each bit position contributes to exactly half of all subsets
        # Total subsets = 2^n, so each bit appears in 2^(n-1) subsets
        return res << (len(nums) - 1)  # Equivalent to res * 2^(n-1)
    
class Solution2:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total):  # Recursive function: i = index, total = current XOR
            if i == len(nums):  # Base case: processed all elements
                return total    # Return the XOR sum of current subset
            # Two choices: include current element or exclude it
            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)
            # Include: XOR with nums[i], Exclude: keep total unchanged
        return dfs(0, 0)  # Start with index 0 and XOR total 0