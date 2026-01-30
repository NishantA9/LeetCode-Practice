from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        res = [1] * (len(nums)) # Initialize the result list with 1s, which will store the final product values                
        prefix = 1 # Initialize prefix product to 1                
        for i in range(len(nums)): # Calculate prefix products and store them in the result list
            res[i] = prefix  # Store the current prefix product in res[i]
            prefix *= nums[i]  # Update prefix to include the current element               
        postfix = 1 # Initialize postfix product to 1                
        for i in range(len(nums) - 1, -1, -1): # Calculate postfix products and multiply them with the corresponding values in res
            res[i] *= postfix  # Multiply the current value in res with the postfix product
            postfix *= nums[i]  # Update postfix to include the current element               
        return res # Return the result list containing the product of all elements except self