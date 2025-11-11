from math import gcd  # import gcd to compute greatest common divisor of lengths
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: # If concatenations differ, there is no common divisor string
            return ""  # no valid gcd string
        g = gcd(len(str1), len(str2)) # gcd of lengths gives length of the largest repeating unit
        return str1[:g]  # prefix of length g is the gcd string