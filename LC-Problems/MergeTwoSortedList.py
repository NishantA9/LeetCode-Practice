# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from typing import ListNode
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # Create a dummy node to serve as the starting point of the merged list
        tail = dummy # Create a pointer (tail) that will be used to build the merged list
        while list1 and list2:  # Iterate through both lists as long as neither is empty
            if list1.val < list2.val: # Compare the current nodes of both lists and attach the smaller one to the merged list
                tail.next = list1   # If the value of the current node in list1 is smaller, attach it to the merged list
                list1 = list1.next  # Move to the next node in list1
            else: # If the value of the current node in list2 is smaller or equal, attach it to the merged list
                tail.next = list2
                list2 = list2.next # Move to the next node in list2
            tail = tail.next  # Move the tail pointer to the newly added node
        if list1: # If there are remaining nodes in list1, attach them to the merged list
            tail.next = list1
        elif list2:  # If there are remaining nodes in list2, attach them to the merged list
            tail.next = list2
        return dummy.next  # Return the merged list, which starts at dummy.next (skipping the dummy node)