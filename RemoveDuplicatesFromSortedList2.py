from typing import Optional
from typing import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node pointing to the head of the list to handle edge cases easily
        dummy = ListNode(0, head)
        # prev is a pointer to the node before the current 'head'
        prev = dummy
        
        # Traverse the linked list
        while head:
            # Check if the current node has a duplicate
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value as 'head'
                while head.next and head.val == head.next.val:
                    head = head.next
                # After the loop, head points to the last node of the duplicates
                # We set prev.next to skip all duplicates
                prev.next = head.next
            else:
                # If no duplicate, just move prev to the next node in the list
                prev = prev.next
            # Move the head pointer to the next node in the list
            head = head.next
        
        # Return the modified list, starting from the original head or new head if duplicates removed
        return dummy.next
