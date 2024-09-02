# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from typing import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the starting point of the merged list
        dummy = ListNode()
        # Create a pointer (tail) that will be used to build the merged list
        tail = dummy

        # Iterate through both lists as long as neither is empty
        while list1 and list2:
            # Compare the current nodes of both lists and attach the smaller one to the merged list
            if list1.val < list2.val:
                # If the value of the current node in list1 is smaller, attach it to the merged list
                tail.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # If the value of the current node in list2 is smaller or equal, attach it to the merged list
                tail.next = list2
                # Move to the next node in list2
                list2 = list2.next
            # Move the tail pointer to the newly added node
            tail = tail.next
        
        # If there are remaining nodes in list1, attach them to the merged list
        if list1:
            tail.next = list1
        # If there are remaining nodes in list2, attach them to the merged list
        elif list2:
            tail.next = list2
        
        # Return the merged list, which starts at dummy.next (skipping the dummy node)
        return dummy.next
