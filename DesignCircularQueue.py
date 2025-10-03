class MyCircularQueue:
    def __init__(self, k: int):
        self.q = []  # List to store queue elements
        self.k = k   # Maximum capacity of the queue
        
    def enQueue(self, value: int) -> bool:
        if len(self.q) == self.k:  # Check if queue is full
            return False
        self.q.append(value)  # Add element to the end of queue
        return True

    def deQueue(self) -> bool:
        if not self.q:  # Check if queue is empty
            return False
        self.q.pop(0)  # Remove element from the front of queue
        return True

    def Front(self) -> int:
        if self.q:
            return self.q[0]  # Return first element
        return -1  # Return -1 if queue is empty

    def Rear(self) -> int:
        if self.q:
            return self.q[-1]  # Return last element
        return -1  # Return -1 if queue is empty

    def isEmpty(self) -> bool:
        return len(self.q) == 0  # Check if queue has no elements

    def isFull(self) -> bool:
        return len(self.q) == self.k  # Check if queue is at maximum capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()