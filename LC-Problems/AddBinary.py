class Solution:
    def addBinary(self, a: str, b: str) -> str:       
        res = "" # build result as string, carry holds carry bit (0/1)
        carry = 0        
        a, b = a[::-1], b[::-1] # reverse inputs to add from least-significant digit (right to left)
        for i in range(max(len(a), len(b))):           
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0 # get digit value if within bounds, otherwise 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0
            total = digitA + digitB + carry  # sum of digits + carry
            char = str(total % 2)  # current result bit
            res = char + res  # prepend to result (or could append and reverse later)
            carry = total // 2  # update carry (0 or 1)        
        if carry: # if leftover carry, prepend it
            res = "1" + res
        return res