# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import ListNode
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head # Initialize two pointers
        while curr:   # Traverse the list
            temp = curr.next           # Temporarily save the next node
            curr.next = prev           # Reverse the current node's pointer
            prev = curr                # Move prev to the current node
            curr = temp                # Move to the next node
        return prev         # prev now points to the new head

# Recursive Solution
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head: # Base case: if head is empty or only one node, return it
#             return None
#         newHead = head # Recursive step: reverse the rest of the list
#         if head.next:
#             newHead = self.reverseList(head.next) # Recursive call
#             head.next.next = head # Make next node point back to the current node
#         head.next = None # Set the current node's next pointer to None
#         return newHead  # newHead is now the new head of the reversed list