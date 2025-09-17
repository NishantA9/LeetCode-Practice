class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []  # Stack to store valid directory names
        cur = ""    # Current directory/file name being read
        for c in path + "/":  # Add trailing '/' to process last part
            if c == "/":  # If we hit a path separator
                if cur == "..":  # Go up one directory if possible
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":  # Ignore empty and '.'
                    stack.append(cur)  # Add valid directory to stack
                cur = ""  # Reset current part
            else:
                cur += c  # Build up current directory/file name
        return "/" + "/".join(stack)  # Join stack to form simplified path