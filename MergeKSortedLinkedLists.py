# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ Merges k sorted linked lists into one sorted linked list using a divide and conquer approach. :param lists: List of ListNode objects representing k sorted linked lists. :return: A single sorted linked list merged from all input lists."""
        if not lists or len(lists) == 0:         # If the input list is empty, return None
            return None 
        
        while len(lists) > 1:  # Repeatedly merge pairs of lists until only one merged list remains
            mergedLists = []  # Temporary list to store merged pairs
            
            for i in range(0, len(lists), 2):  # Iterate over the list in steps of 2, merging pairs of lists
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None  # Ensure we don't go out of bounds
                mergedLists.append(self.mergeList(l1, l2))  # Merge two lists and store      
            lists = mergedLists  # Update lists with newly merged lists
        return lists[0]  # The final merged list

    def mergeList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Merges two sorted linked lists into a single sorted linked list. :param l1: First sorted linked list. :param l2: Second sorted linked list.:return: Merged sorted linked list."""
        dummy = ListNode()  # Dummy node to simplify list merging
        tail = dummy  # Tail pointer to build the new list
        while l1 and l2:         # Merge two lists using a two-pointer approach
            if l1.val < l2.val:
                tail.next = l1  # Append l1 node to merged list
                l1 = l1.next  # Move l1 pointer forward
            else:
                tail.next = l2  # Append l2 node to merged list
                l2 = l2.next  # Move l2 pointer forward
            tail = tail.next  # Move tail pointer forward
        if l1: # If there are remaining nodes in either list, append them
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next  # Return the merged sorted list