class Solution:
    def isValid(self, s: str) -> bool:  # Function to check if the string 's' is valid
        stack = []  # Initialize an empty stack to keep track of opening brackets
        closeToOpen = {")": "(", "]": "[", "}": "{"}  # Map closing brackets to their corresponding opening brackets
        
        # Iterate over each character in the string
        for c in s:
            if c in closeToOpen:  # If the character is a closing bracket
                if stack and stack[-1] == closeToOpen[c]:  
                    # If the stack is not empty and the top of the stack matches the corresponding opening bracket
                    stack.pop()  # Remove the top element from the stack
                else:
                    return False  # If the stack is empty or the top doesn't match, the string is invalid
            else:
                stack.append(c)  # If the character is an opening bracket, add it to the stack
        return True if not stack else False # If the stack is empty at the end, the string is valid