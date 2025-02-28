from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """ Creates a deep copy of a linked list where each node has a random pointer. """
        oldToCopy = {None: None}  # Step 1: Create a HashMap to store the mapping of old nodes to their copies
        cur = head  # Step 2: First pass - Create copies of all nodes without linking them
        while cur:
            copy = Node(cur.val)  # Create a copy of the node
            oldToCopy[cur] = copy  # Store the mapping
            cur = cur.next  # Move to the next node
        cur = head # Step 3: Second pass - Assign next and random pointers
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]  # Set the next pointer
            copy.random = oldToCopy[cur.random]  # Set the random pointer
            cur = cur.next  # Move to the next node
        return oldToCopy[head]         # Step 4: Return the deep copied head