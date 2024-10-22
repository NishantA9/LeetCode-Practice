from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Initialize an array 'arr' with 1 candy for each child
        arr = [1] * len(ratings)
        
        # Left to right pass: ensure that each child with a higher rating than the previous one  gets more candies than the previous child
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                arr[i] = arr[i - 1] + 1
        
        # Right to left pass: ensure that each child with a higher rating than the next one gets more candies than the next child
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)
        
        # Return the sum of the candies distributed to all children
        return sum(arr)
