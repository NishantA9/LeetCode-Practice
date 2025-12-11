class Solution1:
    def minEnd(self, n: int, x: int) -> int:
        res = x  # start with x as the minimal suffix value
        for i in range(n - 1):
            res = (res + 1) | x  # increment then OR with x to maintain required bits
        return res  # final minimal value after n-1 operations
    
#The above code gets time limit exceeded on leetcode.
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x  # baseline value (start with x)
        i_x = 1  # bitmask scanning positions (1,2,4,...)
        i_n = 1  # mask for (n-1) bits to decide which positions to set
        while i_n <= n - 1:  # iterate through bits of (n-1)
            if i_x & x == 0:  # this bit is 0 in x
                if i_n & (n - 1):  # corresponding bit in (n-1) is set
                    res = res | i_x  # set this bit in the result
                i_n = i_n << 1  # advance to next bit of (n-1)
            i_x = i_x << 1  # advance the bitmask position
        return res  # final minimal value