from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Dummy node to simplify edge cases
        groupPrev = dummy  # Pointer to track the previous group's last node
        while True:
            kth = self.getKth(groupPrev, k)            # Find the k-th node from groupPrev
            if not kth:  # If fewer than k nodes remain, stop reversing
                break
            groupNext = kth.next  # Store next group's starting node
            # Reverse the k-group
            prev, curr = kth.next, groupPrev.next  # prev starts at the next group's head
            while curr != groupNext:
                tmp = curr.next  # Store next node
                curr.next = prev  # Reverse current node's pointer
                prev = curr  # Move prev forward
                curr = tmp  # Move curr forward
            # Connect the reversed group to the previous part of the list
            tmp = groupPrev.next  # Store the first node of the current group (which is now last)
            groupPrev.next = kth  # Connect the previous group to the new first node
            groupPrev = tmp  # Move groupPrev to the end of the newly reversed group
        return dummy.next  # Return the modified list

    def getKth(self, curr, k):     # Helper function to get the k-th node from the given node
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr  # Returns k-th node or None if fewer than k nodes remain