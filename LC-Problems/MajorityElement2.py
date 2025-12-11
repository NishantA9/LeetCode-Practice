
from typing import List 
from collections import defaultdict

# Solution class to find majority elements in an array
class Solution:
    # Hashmap approach to find elements appearing more than n/3 times
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}  # Dictionary to store frequency of each number
        # count = Counter(nums) # this will skip the first for loop
        res = []    # List to store result
        for num in nums:
            count[num] = 1 + count.get(num,0)  # Count occurrences
        for key in count:
            if count[key] > len(nums)//3:      # Check if count > n/3
                res.append(key)
        return res

    # Another approach using Boyer-Moore Voting Algorithm
    def majorityElement2(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)  # Dictionary to store up to 2 candidates
        for num in nums:
            count[num] += 1       # Increment count for candidate
            if len(count) <= 2:
                continue         # Only keep up to 2 candidates
            new_count = defaultdict(int)
            for num, c in count.items():
                if c > 1:
                    new_count[num] = c - 1  # Decrement count for all
            count = new_count
        res = []
        for num in count:
            if nums.count(num) > len(nums) // 3:  # Verify actual count
                res.append(num)
        return res