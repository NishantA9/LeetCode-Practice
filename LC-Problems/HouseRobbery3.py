# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # Value of the node (amount of money)
        self.left = left    # Left child node
        self.right = right  # Right child node

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:  # Base case: empty node
                return [0, 0]  # [rob this node, don't rob this node]
            
            leftPair = dfs(root.left)    # Get results from left subtree
            rightPair = dfs(root.right)  # Get results from right subtree
            
            # If we rob current node, we can't rob its children
            withRoot = root.val + leftPair[1] + rightPair[1]
            
            # If we don't rob current node, we can take max from children
            withoutRoot = max(leftPair) + max(rightPair)
            
            return [withRoot, withoutRoot]  # Return both possibilities
        
        return max(dfs(root))  # Return the maximum of robbing or not robbing root