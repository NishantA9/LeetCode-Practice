from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # Initialize an empty list to store the result triplets
        nums.sort() # Sort the input list to make it easier to find triplets

        # Iterate through each number in the list
        for i, a in enumerate(nums):
            # Skip the same number to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1 # Initialize two pointers: one to the right of 'i' and one at the end of the list # noqa: E741
            
            # Use the two-pointer technique to find the other two numbers
            while l < r:
                threeSum = a + nums[l] + nums[r] # Calculate the sum of the current triplet
                if threeSum > 0:
                    r -= 1  # If the sum is greater than zero, move the right pointer leftward
                elif threeSum < 0:
                    l += 1 # If the sum is less than zero, move the left pointer rightward # noqa: E741
                else:
                    res.append([a, nums[l], nums[r]]) # If the sum is zero, add the triplet to the result list
                    l += 1 # Move the left pointer to the right to find the next potential triplet # noqa: E741
                    # Skip duplicates for the second number
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  # noqa: E741
        return res   # Return the list of unique triplets that sum to zero