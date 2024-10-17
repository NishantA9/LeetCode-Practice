from typing import List

#the below sol uses a hashmap to store the count of each element in the list which uses O(n) space and O(n) time
class Solution1:
    def majorityE1ement1(se1f, nums : List [int]) -> int:
        count = {}
        res, maxCount = 0,0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)
        return res

#---------------------------------------------------------------

#the below sol uses Boyer-Moore Voting Algorithm which uses O(1) space and O(n) time
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize the result (majority element) as 0 initially and count as 0.
        res, count = 0, 0
        
        # Iterate through the list of numbers
        for n in nums:
            # If count is 0, set the current element as the majority candidate
            if count == 0:
                res = n
            
            # Update the count:
            # Increment if the current element matches the candidate, otherwise decrement
            count += (1 if n == res else -1)
        
        # Return the majority element that was found
        return res

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