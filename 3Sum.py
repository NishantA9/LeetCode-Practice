from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the result triplets
        res = []
        # Sort the input list to make it easier to find triplets
        nums.sort()
        
        # Iterate through each number in the list
        for i, a in enumerate(nums):
            # Skip the same number to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Initialize two pointers: one to the right of 'i' and one at the end of the list
            l, r = i + 1, len(nums) - 1  # noqa: E741
            
            # Use the two-pointer technique to find the other two numbers
            while l < r:
                # Calculate the sum of the current triplet
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    # If the sum is greater than zero, move the right pointer leftward
                    r -= 1
                elif threeSum < 0:
                    # If the sum is less than zero, move the left pointer rightward
                    l += 1  # noqa: E741
                else:
                    # If the sum is zero, add the triplet to the result list
                    res.append([a, nums[l], nums[r]])
                    # Move the left pointer to the right to find the next potential triplet
                    l += 1  # noqa: E741
                    # Skip duplicates for the second number
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  # noqa: E741
        
        # Return the list of unique triplets
        return res
