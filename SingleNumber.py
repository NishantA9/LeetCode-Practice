from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR-accumulator. Using properties of XOR:
        # a ^ a = 0 and a ^ 0 = a, and XOR is commutative/associative.
        # So XOR-ing all numbers cancels pairs and leaves the single number.
        res = 0
        for num in nums:
            res = num ^ res  # accumulate XOR; paired values cancel out
        return res