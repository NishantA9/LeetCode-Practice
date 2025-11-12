class Solution:
    def multiply(self, num1: str, num2: str) -> str:     
        if "0" in [num1, num2]: # quick zero check: if either input is "0", product is "0"
            return "0"      
        res = [0] * (len(num1) + len(num2)) # result can be at most len(num1) + len(num2) digits        
        num1, num2 = num1[::-1], num2[::-1] # reverse strings to multiply from least-significant digit       
        for i1 in range(len(num1)): # grade-school multiplication: multiply each digit pair and add to res
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])  # product of digit pair
                res[i1 + i2] += digit  # accumulate at the proper offset                
                res[i1 + i2 + 1] += res[i1 + i2] // 10 # carry to next position                
                res[i1 + i2] = res[i1 + i2] % 10 # keep current position single digit  
        res, beg = res[::-1], 0 # reverse back to most-significant first and skip leading zeros
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)