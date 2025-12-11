from collections import deque  # Import deque for queue implementation

class MyStack:

    def __init__(self):
        self.q = deque()  # Initialize a deque to simulate the stack
        
    def push(self, x: int) -> None:
        self.q.append(x)  # Add element to the end of the queue

    def pop(self) -> int:
        # Move all elements except the last to the back of the queue
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())  # Remove from front and add to back
        return self.q.popleft()  # Pop and return the last element (stack top)

    def top(self) -> int:
        return self.q[-1]  # Return the last element (stack top)

    def empty(self) -> bool:
        return len(self.q) == 0  # Check if the queue is empty


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()