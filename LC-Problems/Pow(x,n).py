class Solution:
    def myPow(self, x: float, n: int) -> float:       
        def helper(x, n): # recursive fast power helper: computes x**n for n >= 0            
            if x == 0: # 0 to any power is 0
                return 0            
            if n == 0: # base case: x**0 == 1
                return 1            
            res = helper(x * x, n // 2) # compute (x*x)^(n//2) using divide-and-conquer (square the base, halve the exponent)            
            return x * res if n % 2 else res # if n is odd, multiply by x once more; otherwise the halved result is enough
        res = helper(x, abs(n)) # handle negative exponent by computing with absolute value then inverting if needed
        return res if n >= 0 else 1 / res