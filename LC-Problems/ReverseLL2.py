# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Create dummy node to handle edge cases

        # 1. Reach node at position left
        leftPrev, cur = dummy, head  # leftPrev tracks node before left position
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next  # Move to position left
        # Now cur = left node, leftPrev = node before left
        
        # 2. Reverse nodes from left to right position
        prev = None  # Previous node for reversal
        for i in range(right - left + 1):  # Reverse exactly (right-left+1) nodes
            tmpNext = cur.next  # Store next node
            cur.next = prev     # Reverse the link
            prev, cur = cur, tmpNext  # Move to next pair
        
        # 3. Connect the reversed portion back to the list
        leftPrev.next.next = cur  # Connect end of reversed part to node after right
        leftPrev.next = prev      # Connect node before left to start of reversed part
        return dummy.next  # Return the modified list