# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize a dummy node and pointer
        dummy = ListNode()  # Placeholder node to simplify list creation
        cur = dummy  # Pointer to build the result list
        carry = 0  # Store carry value during addition
        # Step 2: Process both lists until both are empty and carry is 0
        while l1 or l2 or carry:
            # Get the values of the current nodes (if node exists, else 0)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # Step 3: Compute the new digit and carry
            val = v1 + v2 + carry  # Sum of values and carry
            carry = val // 10  # Compute carry for next digit
            val = val % 10  # Extract single digit for current node
            # Step 4: Create a new node with computed value
            cur.next = ListNode(val)
            # Step 5: Move pointers forward
            cur = cur.next  # Move to the new node
            l1 = l1.next if l1 else None  # Move to next node in l1
            l2 = l2.next if l2 else None  # Move to next node in l2
        # Step 6: Return the resulting linked list
        return dummy.next