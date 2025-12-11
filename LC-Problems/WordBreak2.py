from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)  # Convert wordDict to set for O(1) lookup
        def backtrack(i):
            if i == len(s):   # Base case: if we've used the entire string, add current solution
                res.append(" ".join(cur))
                return        
            for j in range(i, len(s)): # Try all possible words starting at index i
                w = s[i:j + 1]   # Extract potential word from current position
                if w in wordDict:  # If it's a valid word, add it to current path and continue
                    cur.append(w)
                    backtrack(j + 1)
                    cur.pop()   # Backtrack: remove word to try other possibilities    
        cur = []         # cur: tracks current sequence of words being built
        res = []         # res: stores all valid word break sequences
        backtrack(0)         # Start backtracking from index 0
        return res