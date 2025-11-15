from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:       
        dp = [0] * (n + 1) # dp[i] will hold the number of 1-bits in binary representation of i     
        offset = 1  # offset is the largest power of two <= current i
        for i in range(1, n + 1):            
            if offset * 2 == i: # when i reaches the next power of two, update offset
                offset = i           
            dp[i] = 1 + dp[i - offset]  # i has one more 1-bit than i - offset (which removes the highest set bit)
        return dp