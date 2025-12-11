import math
class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31, lower 32-bit signed bound
        MAX = 2147483647  #  2^31 - 1, upper 32-bit signed bound
        res = 0  # accumulator for reversed integer
        while x:
            digit = int(math.fmod(x, 10))  # get last digit (works for negatives)
            x = int(x / 10)  # remove last digit (truncating toward zero)            
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10): # overflow check for positive side: if adding digit would exceed MAX
                return 0  # will overflow, return 0 per problem spec            
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10): # overflow check for negative side: if adding digit would go below MIN
                return 0  # will underflow, return 0 per problem spec
            res = (res * 10) + digit  # append digit to reversed result
        return res