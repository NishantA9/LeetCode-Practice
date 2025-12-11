from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {         # Mapping of digits to corresponding letters like a phone keypad
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",   
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(i, curStr):  # Backtracking function to build combinations
            if len(curStr) == len(digits):  # Base case: if the current combination length matches input length
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:  # Recursive case: loop through possible letters for the current digit
                backtrack(i + 1, curStr + c)
        if digits:
            backtrack(0, "")
        return res