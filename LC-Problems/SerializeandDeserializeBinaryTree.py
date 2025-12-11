# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str: # Encodes a tree to a single string.
        res = []  # List to store the tree values in preorder traversal
        def dfs(node):
            if not node:  # If the node is None, add "N" to represent null
                res.append("N")
                return
            res.append(str(node.val))  # Store the node's value
            dfs(node.left)  # Recursively traverse left subtree
            dfs(node.right)  # Recursively traverse right subtree
        dfs(root)  # Start DFS traversal from root
        return ",".join(res)  # Convert list to a comma-separated string
           
    def deserialize(self, data: str) -> Optional[TreeNode]: # Decodes your encoded data to tree.
        vals = data.split(",")  # Split string into list
        self.i = 0  # Index tracker for recursive function
        def dfs():
            if vals[self.i] == "N":  # If "N", return None (null node)
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))  # Create new node
            self.i += 1  # Move index forward
            node.left = dfs()  # Reconstruct left subtree
            node.right = dfs()  # Reconstruct right subtree
            return node  # Return reconstructed node
        return dfs()  # Start reconstruction from index 0