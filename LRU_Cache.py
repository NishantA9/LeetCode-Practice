class Node:
    """ Represents a node in the doubly linked list. Each node stores a key-value pair and pointers to the previous and next nodes. """
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None  # Initialize previous and next pointers as None

class LRUCache:
    """ Implements an LRU (Least Recently Used) Cache using: A HashMap (Dictionary) for O(1) lookup - A Doubly Linked List for efficient removal and insertion"""
    def __init__(self, capacity: int):
        """ Initializes the LRU Cache. :param capacity: The maximum number of key-value pairs the cache can hold."""
        self.cap = capacity  # Store the cache capacity
        self.cache = {}  # Dictionary to map keys to their corresponding node in DLL
        self.left, self.right = Node(0, 0), Node(0, 0)         # Dummy nodes to mark the start (LRU) and end (MRU) of the DLL
        self.left.next, self.right.prev = self.right, self.left  # Connect dummy nodes

    def remove(self, node):
        """Removes a node from the doubly linked list. :param node: The node to remove. """
        prev, nxt = node.prev, node.next  # Get previous and next nodes
        prev.next, nxt.prev = nxt, prev  # Bypass the node to remove it from the list

    def insert(self, node):
        """ Inserts a node at the most recent position (right before the MRU node).:param node: The node to insert."""
        prev, nxt = self.right.prev, self.right  # Get the last node and MRU node
        prev.next = nxt.prev = node  # Connect the new node
        node.next, node.prev = nxt, prev  # Adjust new node's pointers

    def get(self, key: int) -> int:
        """ Retrieves a value from the cache and moves the accessed node to the MRU position. :param key: The key to look up. :return: The value associated with the key, or -1 if the key is not found. """
        if key in self.cache:  # Key exists in the cache
            self.remove(self.cache[key])  # Remove it from its current position
            self.insert(self.cache[key])  # Reinsert it as the most recently used
            return self.cache[key].val  # Return the stored value
        return -1  # Key not found in cache

    def put(self, key: int, value: int) -> None:
        """ Adds a key-value pair to the cache. If the key exists, updates its value. If the cache exceeds capacity, removes the least recently used (LRU) item.
        :param key: The key to store.:param value: The value associated with the key. """
        if key in self.cache:  # If key already exists, remove the old node
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)  # Create new node
        self.insert(self.cache[key])  # Insert at MRU position
        if len(self.cache) > self.cap:  # If cache exceeds capacity, remove LRU
            lru = self.left.next  # Get the least recently used node (leftmost)
            self.remove(lru)  # Remove LRU node from DLL
            del self.cache[lru.key]  # Remove LRU node from HashMap
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)            