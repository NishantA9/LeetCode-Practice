from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []  # Initialize the result list
        for i in range(2):  # Loop runs 2 times to simulate x = 2 concatenations
            for num in nums:
                ans.append(num)  # Append each element from nums
        return ans  # Final array: nums + nums
    
# another way to do it:
class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2  # Concatenate the list with itself using multiplication or add operator like nums + nums
    
# what if you have k concatenations?
class Solution3:
    def getConcatenation(self, nums: List[int], k: int) -> List[int]:
        ans = []  # Initialize the result list
        for i in range(k):
            for num in nums:
                ans.append(num)
        return ans