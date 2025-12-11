from typing import Optional, TreeNode # For type hinting

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive solution to evaluate a boolean binary tree.
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # If this is a leaf node (no left and right child), return its boolean value.
        if not root.left and not root.right:
            # Return True if the value is 1, otherwise return False (since leaf nodes are 1 or 0).
            return root.val == 1
        
        # If the current node's value is 2, it represents an OR operator.
        if root.val == 2:
            # Recursively evaluate the left and right children, apply OR logic.
            return(
                self.evaluateTree(root.left) or  # True if either child is True
                self.evaluateTree(root.right)
            )
        
        # If the current node's value is 3, it represents an AND operator.
        if root.val == 3:
            # Recursively evaluate the left and right children, apply AND logic.
            return(
                self.evaluateTree(root.left) and  # True only if both children are True
                self.evaluateTree(root.right)
            )

# ------------------------------------------

#Iterative solution to evaluate a boolean binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution1:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # Initialize a stack to perform iterative tree traversal
        # The stack will help to visit nodes one by one
        stack = [root]
        
        # Dictionary to store evaluated boolean values for each node
        value = {}  # Stores node -> boolean result (True/False)

        # Start traversing the tree using the stack
        while stack:
            # Pop a node from the top of the stack to evaluate it
            node = stack.pop()
            
            # If the node is a leaf (i.e., it has no left or right children)
            if not node.left and not node.right:
                # For leaf nodes, store the boolean value directly based on node's value
                # If node value is 1, it is True, otherwise it is False
                value[node] = node.val == 1

            # If the node is not a leaf (internal node with children)
            else:
                # Check if both left and right children have already been evaluated
                if node.left in value and node.right in value:
                    # If the current node represents an OR operation (value 2)
                    if node.val == 2:
                        # Apply the OR operation on the results of the left and right children
                        value[node] = value[node.left] or value[node.right]

                    # If the current node represents an AND operation (value 3)
                    if node.val == 3:
                        # Apply the AND operation on the results of the left and right children
                        value[node] = value[node.left] and value[node.right]
                
                # If the children are not evaluated yet, push the current node back onto the stack
                # along with its children (right and left), so we can evaluate them first.
                else:
                    # Re-push the current node to the stack so we can evaluate it later
                    # after its children have been evaluated.
                    stack.extend([node, node.right, node.left])

        # Return the evaluated boolean value of the root node (the overall result of the tree)
        return value[root]

            
          