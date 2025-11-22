from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head  # initialize slow and fast pointers at head
        while fast and fast.next:  # continue until fast reaches the end
            slow = slow.next  # move slow by 1
            fast = fast.next.next  # move fast by 2
        return slow  # slow will be at middle node (second middle for even length)