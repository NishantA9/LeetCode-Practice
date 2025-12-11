# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head         # Initialize two pointers, both starting from the head
        while fast and fast.next:         # Traverse the list until fast or fast.next becomes None
            slow = slow.next          # Move slow pointer by 1 step
            fast = fast.next.next     # Move fast pointer by 2 steps
            if slow == fast:             # If pointers meet, a cycle is detected
                return True
        return False        # If the loop ends, no cycle is present