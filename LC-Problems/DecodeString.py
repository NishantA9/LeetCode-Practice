class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # Stack to keep track of characters and substrings
        for i in range(len(s)):
            if s[i] != "]":  # If not closing bracket, push to stack
                stack.append(s[i])
            else:
                substr = ""  # To build the substring inside brackets
                while stack[-1] != "[":  # Pop until opening bracket
                    substr = stack.pop() + substr
                stack.pop()  # Remove the opening bracket '['

                k = ""  # To build the repeat count
                while stack and stack[-1].isdigit():  # Pop digits for repeat count
                    k = stack.pop() + k
                stack.append(int(k) * substr)  # Repeat substring and push back
        return "".join(stack)  # Join everything for the final result