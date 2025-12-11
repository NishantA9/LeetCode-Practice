from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result list with 1s, which will store the final product values
        res = [1] * (len(nums))
        
        # Initialize prefix product to 1
        prefix = 1
        
        # Calculate prefix products and store them in the result list
        for i in range(len(nums)):
            res[i] = prefix  # Store the current prefix product in res[i]
            prefix *= nums[i]  # Update prefix to include the current element
        
        # Initialize postfix product to 1
        postfix = 1
        
        # Calculate postfix products and multiply them with the corresponding values in res
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix  # Multiply the current value in res with the postfix product
            postfix *= nums[i]  # Update postfix to include the current element
        
        # Return the result list containing the product of all elements except self
        return res
