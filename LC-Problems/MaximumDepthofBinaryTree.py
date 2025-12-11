# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:         # Base case: if the root is None, return 0 (empty tree)
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))  # Recursively calculate the max depth of left and right subtrees
    
#---------------------------------------- Iterative Solution using DFS (Stack) ----------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:  # Edge case: if root is None, return 0
            return 0
        stack = [[root, 1]]  # Stack to store nodes along with their current depth
        res = 0
        while stack:
            node, depth = stack.pop()  # Get current node and its depth
            if node:
                res = max(res, depth)  # Update the maximum depth encountered so far
                stack.append([node.left, depth + 1])   # Push left and right children onto the stack with incremented depth
                stack.append([node.right, depth + 1])
        return res  # Return the maximum depth found

#---------------------------------------- Breadth-First Search (BFS) using Queue ----------------------------------------


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution3:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque() # Initialize a queue for BFS traversal
        if root:  # If the tree is not empty, add the root node to the queue
            q.append(root)
        level = 0  # Track the depth of the tree
        while q:
            for i in range(len(q)):  # Process all nodes at the current level
                node = q.popleft()  # Remove node from queue
                if node.left:  # Add left and right children to the queue (if they exist)
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1  # Increment the level after processing all nodes at the current level
        return level # Return the final depth of the tree  