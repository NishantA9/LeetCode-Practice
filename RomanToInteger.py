class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000} # HashMap to store Roman numeral values        
        res = 0  # Variable to store the result       
        for i in range(len(s)): # Iterate through each character in the string
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]: # If the current character is smaller than the next, subtract its value
                res -= roman[s[i]]
            else:                
                res += roman[s[i]] # Otherwise, add its value        
        return res  # Return the final result