from typing import List
#the below sol uses a hashmap to store the count of each element in the list which uses O(n) space and O(n) time
class Solution1:
    def majorityE1ement1(se1f, nums : List [int]) -> int:
        count = {}  # Dictionary to store frequency of each number
        res, maxCount = 0, 0  # res stores the current majority, maxCount tracks its frequency
        for n in nums:
            count[n] = 1 + count.get(n, 0)  # Count occurrences of n
            if count[n] > maxCount:  # Update majority if current count exceeds max
                res = n
                maxCount = count[n]
        return res  # Return the number that appears more than ⌊n / 2⌋ times

#---------------------------------------------------------------

#the below sol uses Boyer-Moore Voting Algorithm which uses O(1) space and O(n) time
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0 # Initialize the result (majority element) as 0 initially and count as 0.
        for n in nums:  # Iterate through the list of numbers
            if count == 0: # If count is 0, set the current element as the majority candidate
                res = n
            count += (1 if n == res else -1) # Update the count: Increment if the current element matches the candidate, otherwise decrement
        return res  # Return the majority element that was found
'''
Example Walkthrough:
For input nums = [3, 3, 4, 2, 3, 3, 3]:

Initially, res = 0 and count = 0.
As the algorithm processes the list:
First element 3: Since count == 0, res becomes 3, and count becomes 1.
Next element 3: count increases to 2.
Next element 4: count decreases to 1 (since 4 != res).
Next element 2: count decreases to 0.
Next element 3: Since count == 0, res becomes 3 again, and count becomes 1.
Next elements 3 and 3: count increases to 3.
The algorithm concludes that the majority element is 3.

'''