from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0  # counts of $5 and $10 bills we have
        for b in bills:
            if b == 5:
                five += 1  # accept $5, increase $5 count
            elif b == 10:
                five, ten = five - 1, ten + 1  # give one $5 as change, keep one $10
            elif ten > 0:
                five, ten = five - 1, ten - 1  # prefer giving $10 + $5 as change
            else:
                five -= 3  # give three $5 bills as change
            if five < 0:
                return False  # not enough change
        return True  # served all customers successfully