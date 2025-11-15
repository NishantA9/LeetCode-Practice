class Solution:
    def reverseBits(self, n: int) -> int:     
        res = 0 # build reversed-bit integer     
        for i in range(32): # iterate over 32 bits (from least-significant to most-significant)          
            bit = (n >> i) & 1 # extract the i-th bit of n            
            res += (bit << (31 - i)) # place it at the reversed position (31 - i) and add to result
        return res