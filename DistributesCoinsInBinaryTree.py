from typing import Optional, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # Initialize a result variable to track the total number of moves required.
        self.res = 0
        
        # Define the depth-first search (dfs) recursive function to calculate extra coins.
        def dfs(cur):
            # Base case: if the current node is None (null), return 0 extra coins.
            if not cur:
                # In the previous approach, we returned both size and coins (commented out below)
                # return [0, 0] #[size, coins]
                # However, in the optimized method, we only track extra coins.
                return 0 # No extra coins for a null node.

            # Recursive case: traverse the left and right children and get their extra coins.
            left_extra = dfs(cur.left)
            right_extra = dfs(cur.right)
            
            # Calculate the extra coins at the current node:
            # The formula is: (current node's coins - 1) + left_extra + right_extra
            # cur.val is the number of coins at this node, and -1 accounts for the 1 coin each node should have.
            extra_coins = cur.val - 1 + left_extra + right_extra
            
            # Update the total moves by adding the absolute value of extra_coins.
            # If extra_coins is positive, it means excess coins need to be moved out.
            # If negative, it means coins need to be moved into the node.
            self.res += abs(extra_coins)
            
            # Return the extra coins at this node so the parent node can balance.
            return extra_coins

        # Start the depth-first search from the root node.
        dfs(root)
        
        # Return the total number of moves required to balance the coins.
        return self.res
        
        
# -----------------------------------------------------------------------

# from typing import Optional, TreeNode

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def distributeCoins(self, root: Optional[TreeNode]) -> int:
#         self.res = 0
#         def dfs(cur):
#             if not cur:
#                 #previous method
#                 #optimized method
#                 return 0 #extra coins
            
#             #previous method
#             # left_size, left_coins = dfs(cur.left)
#             # right_size, right_coins = dfs(cur.right)
#             # size = 1 + left_size + right_size
#             # coins = cur.val + left_coins + right_coins
#             # self.res += abs(coins - size)
#             # return [size, coins]
            
#             #optimize method
#             left_extra = dfs(cur.left)
#             right_extra = dfs(cur.right)
#             extra_coins = cur.val - 1 + left_extra + right_extra
#             self.res += abs(extra_coins)
#             return extra_coins
#         dfs(root)
#         return self.res