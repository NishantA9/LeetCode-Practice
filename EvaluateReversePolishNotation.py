from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Initialize an empty stack to store numbers
        
        # Loop through each token in the input list
        for c in tokens:
            if c == "+":  # If the token is "+", pop two numbers and add them
                stack.append(stack.pop() + stack.pop())
            elif c == "-":  # If the token is "-", pop two numbers and subtract
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)  # Note: b is subtracted by a
            elif c == "*":  # If the token is "*", pop two numbers and multiply
                stack.append(stack.pop() * stack.pop())
            elif c == "/":  # If the token is "/", pop two numbers and divide
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))  # Use int() to truncate towards zero
            else:  # If the token is a number, push it onto the stack
                stack.append(int(c))
        return stack[0]         # The final result will be the only number left in the stack