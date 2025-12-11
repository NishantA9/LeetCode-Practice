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

#---------------------------------------------------------------------------------------------------        
#DFS solution
class SolutionDFS:
        def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            res = [] 
            def dfs(node,depth):
                if not node: # Base case: if the node is None, return
                    return None
                if len(res) == depth: # If we're at a new depth, add a new list to res
                    res.append([])
                res[depth].append(node.val) # Append the current node's value to its depth level
                dfs(node.left, depth + 1) # Traverse the left and right subtrees with increased depth
                dfs(node.right, depth + 1)
                dfs(root,0) # Start DFS from root at depth 0
            return res 