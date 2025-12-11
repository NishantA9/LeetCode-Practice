class Solution:
    def intToRoman(self, num: int) -> str:
        # List of Roman numeral symbols paired with their integer values
        symList = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
            ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
            ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
            ["M", 1000]
        ]
        
        res = ""  # This will store the resulting Roman numeral string
        
        # Iterate over the symbols from largest to smallest (hence, reversed)
        for sym, val in reversed(symList):
            # Check how many times the current Roman symbol fits into 'num'
            if num // val:
                count = num // val  # Calculate how many times we can use this symbol
                
                # Append the symbol 'count' times to the result string
                res += (sym * count)
                
                # Update 'num' to the remainder after using the current symbol
                num = num % val
        
        return res  # Return the final Roman numeral string
