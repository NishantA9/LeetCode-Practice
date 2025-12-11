from typing import List
class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index     # Initialize a hashmap to store value and its index
        for i, n in enumerate(nums):    # Iterate over the list of numbers
            diff = target - n     # Calculate the difference needed to reach the target
            if diff in prevMap:     # Check if the difference exists in the hashmap
                return [prevMap[diff], i]     # If it exists, return the indices of the two numbers
            prevMap[n] = i    # Store the value and its index in the hashmap
        return []    # Return an empty list if no solution is found

'''
# 🔁 Modified Code: Return All Unique Pairs of Indices

def allTwoSums(nums, target):
    seen = {}
    result = []
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            result.append([seen[diff], i])  # Append each valid pair
        seen[n] = i        # Always update seen after the check to avoid using the same number twice
    return result
'''