from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []  # Initialize the result list
        for i in range(2):  # Loop runs 2 times to simulate x = 2 concatenations
            for num in nums:
                ans.append(num)  # Append each element from nums
        return ans  # Final array: nums + nums