class FreqStack:

    def __init__(self):
        self.cnt = {}      # Dictionary to count frequency of each value
        self.maxcnt = 0    # Track the current maximum frequency
        self.stack = {}    # Dictionary: freq -> list of values with that freq
        
    def push(self, val: int) -> None:
        valcnt = 1 + self.cnt.get(val,0)  # Increment frequency for val
        self.cnt[val] = valcnt  # Update frequency count
        if valcnt > self.maxcnt:
            self.maxcnt = valcnt  # Update max frequency if needed
            self.stack[valcnt] = []  # Create new stack for this frequency
        self.stack[valcnt].append(val)  # Add value to its frequency stack

    def pop(self) -> int:
        res = self.stack[self.maxcnt].pop()  # Pop most frequent value
        self.cnt[res] -= 1  # Decrease its frequency
        if not self.stack[self.maxcnt]:  # If no more at this freq
            self.maxcnt -= 1  # Decrease max frequency
        return res  # Return the popped value

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()