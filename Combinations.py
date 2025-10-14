from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []  # Result list to store all combinations        
        def backtrack(start, comb):  # start: next number to consider, comb: current combination
            if len(comb) == k:  # Base case: combination is complete
                res.append(comb.copy())  # Add copy of current combination to result
                return            
            # Try all numbers from start to n
            for i in range(start, n + 1):
                comb.append(i)       # Include current number in combination
                backtrack(i + 1, comb)  # Recursively build rest of combination
                comb.pop()           # Backtrack: remove current number        
        backtrack(1, [])  # Start with number 1 and empty combination
        return res        # Return all generated combinations