from typing import List
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool: #TC: O(N) & SC: O(1)
        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]: # Skip if any element exceeds the target value
                continue
            for i,v in enumerate(t): # Add indices where the triplet matches the target value
                if v == target[i]:
                    good.add(i) 
        return len(good) == 3   # Check if we found matching values for all 3 positions          