# Definition for a binary tree node.
import collections  # Import the collections module for deque
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # Stores the final level order traversal result
        q = collections.deque()  # Create a queue for BFS traversal
        q.append(root)  # Start with the root node
        while q:  # Continue traversal until the queue is empty
            qLen = len(q)  # Number of nodes at the current level
            level = []  # List to store node values at the current level
            for i in range(qLen):  # Process all nodes at the current level
                node = q.popleft()  # Remove the front node from the queue
                if node:  
                    level.append(node.val)  # Add node value to the level list
                    q.append(node.left)  # Add left child to the queue
                    q.append(node.right)  # Add right child to the queue
            if level:  
                res.append(level)  # Add the current level to the result
        return res  # Return the level order traversal result