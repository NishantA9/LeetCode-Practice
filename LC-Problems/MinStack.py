class MinStack:

    def __init__(self):
        self.stack = [] # Initialize two stacks:  - 'stack' for storing all values.
        self.minstack = []  # - 'minstack' for keeping track of the minimum value at each point.

    def push(self, val: int) -> None:
        self.stack.append(val)  # Push the value onto the main stack
        # Determine the new minimum value: - If 'minstack' is empty, the new minimum is the value itself. - Otherwise, it's the smaller of the current value and the top of 'minstack'.
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val) # Push the new minimum value onto 'minstack'

    def pop(self) -> None:
        self.stack.pop() # Remove the top element from both 'stack' and 'minstack'
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]  # Return the top element of 'stack'

    def getMin(self) -> int:
        return self.minstack[-1] # Return the top element of 'minstack' (the current minimum value)

# Example usage:
# obj = MinStack()         # Create a new MinStack object
# obj.push(val)            # Push a value onto the stack
# obj.pop()                # Pop the top element from the stack
# param_3 = obj.top()      # Retrieve the top element of the stack
# param_4 = obj.getMin()   # Retrieve the minimum element in the stack
