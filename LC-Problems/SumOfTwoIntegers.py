class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # mask to get 32-bit truncation
        max_int = 0x7FFFFFFF  # max signed 32-bit int
        while b != 0:
            carry = (a & b) << 1  # carry bits (where both bits are 1), shifted
            a = (a ^ b) & mask  # sum without carry (xor), truncated to 32 bits
            b = carry & mask  # next carry to add in following iteration
        return a if a <= max_int else ~(a ^ mask)  # convert to signed int if needed