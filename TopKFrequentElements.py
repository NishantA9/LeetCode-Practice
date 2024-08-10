from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize a dictionary to count the frequency of each number in nums
        count = {}
        
        # Initialize a list of empty lists, where the index represents the frequency
        # The list is sized len(nums) + 1 because the max frequency a number can have is len(nums)
        freq = [[] for i in range(len(nums) + 1)]
        
        # Count the frequency of each number in nums
        for n in nums:
            count[n] = 1 + count.get(n, 0)  # Increment the count for each number
        
        # Group numbers by their frequency in the freq list
        for n, c in count.items():
            freq[c].append(n)  # Append the number n to the list at index c
        
        # Initialize the result list to store the top k frequent elements
        res = []
        
        # Iterate over the freq list in reverse order (from highest to lowest frequency)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:  # Go through each number with the current frequency
                res.append(n)  # Add the number to the result list
                if len(res) == k:  # If we've added k elements, return the result
                    return res
