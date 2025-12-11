from collections import defaultdict

class ListNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val      # Value stored in the node
        self.prev = prev    # Previous node in the doubly linked list
        self.next = next    # Next node in the doubly linked list

class LinkedList:

    def __init__(self):
        self.left = ListNode(0)  # Dummy head node
        self.right = ListNode(0, self.left)  # Dummy tail node
        self.left.next = self.right  # Connect head to tail
        self.map = {}  # Map value to node for O(1) access

    def length(self):
        return len(self.map)  # Return number of nodes in the list

    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)  # Create new node
        self.map[val] = node  # Store node in map for O(1) access
        self.right.prev = node  # Update tail's previous
        node.prev.next = node   # Update previous node's next

    def pop(self, val):
        if val in self.map:  # Check if value exists
            node = self.map[val]  # Get the node
            next, prev = node.next, node.prev  # Get neighbors
            next.prev = prev  # Update next node's previous
            prev.next = next  # Update previous node's next
            self.map.pop(val, None)  # Remove from map

    def popLeft(self):
        res = self.left.next.val  # Get leftmost value
        self.pop(self.left.next.val)  # Remove leftmost node
        return res  # Return the value

    def update(self, val):
        self.pop(val)        # Remove from current position
        self.pushRight(val)  # Add to the right (most recent)

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity  # Maximum capacity of the cache
        self.lfuCnt = 0      # Current minimum frequency count
        self.valMap = {}     # Map key -> val
        self.countMap = defaultdict(int)  # Map key -> count
        # Map count of key -> linkedlist
        self.listMap = defaultdict(LinkedList)

    def counter(self, key):
        cnt = self.countMap[key]  # Get current frequency
        self.countMap[key] += 1   # Increment frequency
        self.listMap[cnt].pop(key)  # Remove from old frequency list
        self.listMap[cnt + 1].pushRight(key)  # Add to new frequency list

        # If old frequency list is empty and it was the minimum, increment min
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1


    def get(self, key: int) -> int:
        if key not in self.valMap:  # Key doesn't exist
            return -1
        self.counter(key)  # Update frequency count
        return self.valMap[key]  # Return the value

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:  # No capacity
            return

        # If cache is full and key is new, evict LFU key
        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCnt].popLeft()  # Remove LFU key
            self.valMap.pop(res)    # Remove from value map
            self.countMap.pop(res)  # Remove from count map

        self.valMap[key] = value  # Store/update the value
        self.counter(key)         # Update frequency
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])  # Update min frequency