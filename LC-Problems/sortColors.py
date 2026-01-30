from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3  # counts for 0, 1, and 2
        for num in nums:  # tally each number's occurrences
            count[num] += 1  # increment count for this value
        index = 0  # position to write next value into nums
        for i in range(3):  # for each color/value 0, 1, 2
            while count[i]:  # while there are remaining of color i
                nums[index] = i  # place color i at current index
                index += 1  # advance write index
                count[i] -= 1  # decrement remaining count for i