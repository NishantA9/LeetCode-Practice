#import ListNode from typing
from typing import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Initialize result to store the decimal value
        res = 0
        # Traverse the linked list
        while head:
            # Multiply the current result by 2 (shift left in binary)
            res *= 2
            # Add the current node's value to result
            res += head.val
            # Move to the next node in the list
            head = head.next
        # Return the final decimal value
        return res
