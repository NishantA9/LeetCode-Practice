from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one = 1  # the '1' we want to add
        i = 0  # index in reversed list
        digits.reverse()  # work from least-significant digit first
        while one:  # propagate carry while there's a 1 to add
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0  # 9 + 1 -> 0 with carry
                else:
                    digits[i] += 1  # add carry and stop
                    one = 0
            else:
                digits.append(one)  # extend array if carry remains past highest digit
                one = 0
            i += 1  # move to next digit
        digits.reverse()  # restore original order
        return digits  # result