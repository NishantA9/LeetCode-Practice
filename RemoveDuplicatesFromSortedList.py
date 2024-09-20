from typing import Optional
from typing import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize current node pointer to the head of the list
        cur = head
        
        # Traverse the list until we reach the end
        while cur:
            # Check if the next node exists and has the same value as the current node
            while cur.next and cur.next.val == cur.val:
                # If duplicate found, skip the next node
                cur.next = cur.next.next
            
            # Move to the next node
            cur = cur.next
        
        # Return the modified list with duplicates removed
        return head
