class MyQueue:
    def __init__(self):
        self.s1 = []  # Stack for incoming elements
        self.s2 = []  # Stack for outgoing elements
        
    def push(self, x: int) -> None:
        self.s1.append(x)  # Always push to s1
        
    def pop(self) -> int:
        if not self.s2:  # If s2 is empty, transfer all from s1
            while self.s1:
                self.s2.append(self.s1.pop())  # Reverse order for queue behavior
        return self.s2.pop()  # Pop from s2 (front of queue)

    def peek(self) -> int:
        if not self.s2:  # If s2 is empty, transfer all from s1
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]  # Peek at the front of the queue
        
    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0  # True if both stacks are empty

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()