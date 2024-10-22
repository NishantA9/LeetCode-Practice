class Solution:
    def romanToInt(self, s: str) -> int:
        # HashMap to store Roman numeral values
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        res = 0  # Variable to store the result
        
        # Iterate through each character in the string
        for i in range(len(s)):
            # If the current character is smaller than the next, subtract its value
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                # Otherwise, add its value
                res += roman[s[i]]
        
        return res  # Return the final result
