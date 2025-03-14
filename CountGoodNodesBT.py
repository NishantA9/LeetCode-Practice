# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0  # Base case: If node is None, return 0
            res = 1 if node.val >= maxVal else 0             # Check if current node is a "good node"
            maxVal = max(maxVal, node.val) # Update maxVal to the max seen so far
            res += dfs(node.left, maxVal) # Recur for left and right subtrees and count good nodes
            res += dfs(node.right, maxVal)
            return res  # Return total count of good nodes
        return dfs(root, root.val) # Start DFS from root with initial max value as root's value