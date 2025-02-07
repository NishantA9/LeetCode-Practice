#Rules for this problem:
# 1. Only add open paranthesis if open < n
# 2. Only add close paranthesis if close < open
# 3. If open == n and close == n, add the string to the result as its valid paranthesis
#we are doing it in recursively so we need to keep track of the open and close paranthesis
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] # Stack to keep track of the current combination being built
        res = [] # Result list to store all valid combinations

        # Helper function for backtracking # `openN` is the number of '(' used so far  # `closeN` is the number of ')' used so far
        def backtrack(openN, closeN):
            if openN == closeN == n: # Base case: If we've used all n '(' and n ')', add the combination to the result
                res.append("".join(stack))  # Convert the stack to a string
                return

            if openN < n:# If we can still add an opening parenthesis '('
                stack.append("(")            # Add '(' to the stack
                backtrack(openN + 1, closeN) # Recurse with one more '('
                stack.pop()                  # Remove '(' after exploring this path
                       
            if closeN < openN:  # If we can still add a closing parenthesis ')' # Note: We can only add ')' if `closeN` is less than `openN`
                stack.append(")")            # Add ')' to the stack
                backtrack(openN, closeN + 1) # Recurse with one more ')'
                stack.pop()                  # Remove ')' after exploring this path

        backtrack(0, 0) # Start the backtracking with 0 '(' and 0 ')'
        return res # Return the list of valid combinations