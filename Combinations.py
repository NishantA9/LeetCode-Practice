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
    
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []  # Result list to store all combinations
        def backtrack(i, comb):  # i: current number to consider, comb: current combination
            if i > n:  # Base case: exceeded the range of numbers
                if len(comb) == k:  # Check if we have exactly k elements
                    res.append(comb.copy())  # Add valid combination to result
                return           
            # Decision 1: Include current number i in combination
            comb.append(i)          # Add current number
            backtrack(i + 1, comb)  # Recurse with next number
            comb.pop()              # Backtrack: remove current number          
            # Decision 2: Skip current number i (don't include it)
            backtrack(i + 1, comb)  # Recurse with next number without including i        
        backtrack(1, [])  # Start with number 1 and empty combination
        return res        # Return all generated combinations