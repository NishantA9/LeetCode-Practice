# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root  # Start from the root node
        while cur:
            if p.val > cur.val and q.val > cur.val: # If both p and q are greater than cur, LCA is in the right subtree
                cur = cur.right  
            elif p.val < cur.val and q.val < cur.val: # If both p and q are smaller than cur, LCA is in the left subtree
                cur = cur.left  
            else:  # If p and q are on different sides, or one of them is cur itself, cur is the LCA
                return cur