from typing import Optional, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# RECURSIVE SOLUTION
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # Base case: if the root is None (empty tree), return None.
        if not root:
            return None
        
        # Recursively process the left subtree and update the left child of the current node.
        root.left = self.removeLeafNodes(root.left, target)
        
        # Recursively process the right subtree and update the right child of the current node.
        root.right = self.removeLeafNodes(root.right, target)
        
        # If the current node becomes a leaf and its value equals the target, remove the node (return None).
        if not root.left and not root.right and root.val == target:
            return None
        
        # If the node is not removed, return the current node.
        return root

          
# -------------------------------------------------------        
# ITERATIVE SOLUTION

class Solution1:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # Stack for iterative DFS traversal.
        stack = [root]
        
        # Set to track visited nodes.
        visited = set()
        
        # Dictionary/hashmap to keep track of parent nodes. Initially, the root's parent is None.
        parent = {root: None}
        
        # Start iterating over the stack until it's empty.
        while stack:
            # Pop a node from the stack to process.
            node = stack.pop()
            
            # If the node is a leaf (no children), check if its value equals the target.
            if not node.left and not node.right:
                if node.val == target:
                    # Get the parent of the current node.
                    p = parent[node]
                    
                    # If there is no parent (node is the root), return None.
                    if not p:
                        return None
                    
                    # If the node is a left child of its parent, remove it by setting parent's left to None.
                    if p.left == node:
                        p.left = None
                    
                    # If the node is a right child of its parent, remove it by setting parent's right to None.
                    if p.right == node:
                        p.right = None
            
            # If the node isn't a leaf, ensure it's revisited after processing its children.
            elif node not in visited:
                visited.add(node)
                
                # Push the node back onto the stack (it will be revisited after children).
                stack.append(node)
                
                # Push the right child onto the stack (if it exists) and track the parent relationship.
                if node.right:
                    stack.append(node.right)
                    parent[node.right] = node
                
                # Push the left child onto the stack (if it exists) and track the parent relationship.
                if node.left:
                    stack.append(node.left)
                    parent[node.left] = node
        
        # Finally, return the updated root of the tree.
        return root
