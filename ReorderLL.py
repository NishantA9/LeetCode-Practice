from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Rearranges the linked list in a specific alternating pattern.
        """
        if not head or not head.next:
            return  # No need to reorder if there's 0 or 1 node

        # Step 1: Find the middle of the list using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        second = slow.next  # Second half starts after the middle
        prev = slow.next = None  # Disconnect the two halves

        while second:
            tmp = second.next  # Save next node
            second.next = prev  # Reverse link
            prev = second  # Move prev pointer forward
            second = tmp  # Move second pointer forward

        # Step 3: Merge the two halves
        first, second = head, prev  # `second` is now the reversed half
        while second:  # While there are nodes in the second half
            tmp1, tmp2 = first.next, second.next  # Save next nodes
            first.next = second  # Connect first node to a node from the reversed half
            second.next = tmp1  # Connect the reversed node to the next node in first half
            first, second = tmp1, tmp2  # Move both pointers forward