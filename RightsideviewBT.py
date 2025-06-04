# Definition for a binary tree node.
import collections 
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # List to store the right-side view
        q = collections.deque([root])  # Initialize queue with the root
        while q:
            rightSide = None  # Stores the rightmost node in the level
            qLen = len(q)  # Number of nodes in the current level
            for i in range(qLen):  # Iterate through the current level
                node = q.popleft()  # Remove the front node from queue
                if node:
                    rightSide = node  # Update rightmost node for this level
                    q.append(node.left)  # Add left child to queue
                    q.append(node.right)  # Add right child to queue
            if rightSide:
                res.append(rightSide.val)  # Add last node of level to result
        return res  # Return the right-side view of the tree

#---------------------------------------------------------------------------------------------------    
#DFS solution
class SolutionDFS:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node, depth):
            if not node: # Base case: if the current node is None, return
                return None
            if depth == len(res):# If this is the first node we're visiting at this depth, it's the rightmost one (because we visit right first)
                res.append(node.val)
            dfs(node.right, depth + 1) # First go right (to catch rightmost nodes first)
            dfs(node.left, depth + 1)# Then go left
        dfs(root, 0)
        return res