from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the N-th node from the end of the list and returns the modified list.
        """
        dummy = ListNode(0, head) # Step 1: Create a dummy node before the head
        left = dummy  # Left pointer starts at dummy
        right = head  # Right pointer starts at head
        while n > 0 and right:  # Step 2: Move the right pointer 'n' steps ahead
            right = right.next
            n -= 1
        while right:  # Step 3: Move both pointers until right reaches the end
            left = left.next
            right = right.next
        left.next = left.next.next   # Step 4: Remove the N-th node by skipping it  
        return dummy.next         # Return the modified list starting from dummy.next (head)