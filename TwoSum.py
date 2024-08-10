from typing import List

class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Initialize a hashmap to store value and its index
        prevMap = {}  # val : index
    # Iterate over the list of numbers
        for i, n in enumerate(nums):
    # Calculate the difference needed to reach the target
            diff = target - n
     # Check if the difference exists in the hashmap
            if diff in prevMap:
    # If it exists, return the indices of the two numbers
                return [prevMap[diff], i]
    # Store the value and its index in the hashmap
            prevMap[n] = i
    # Return an empty list if no solution is found
        return []
    