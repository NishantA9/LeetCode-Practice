from typing import List  # Correct import for List
class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		prefix = {0: 1}  # Dictionary to store prefix sums and their counts
		curSum = 0       # Current prefix sum
		res = 0          # Result to count subarrays
		for num in nums:
			curSum += num  # Add current number to prefix sum
			diff = curSum - k  # Find the needed sum to reach k
			res += prefix.get(diff, 0)  # Add count if such prefix exists
			prefix[curSum] = 1 + prefix.get(curSum, 0)  # Update prefix count
		return res  # Return total count of subarrays