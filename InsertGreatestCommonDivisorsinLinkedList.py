# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            # compute gcd using Euclidean algorithm
            while b > 0:
                a, b = b, a % b
            return a
        cur = head  # pointer to traverse list
        while cur.next:  # while there's a next node to compute gcd with
            n1, n2 = cur.val, cur.next.val  # adjacent node values
            # insert new node with gcd between cur and cur.next
            cur.next = ListNode(gcd(n1, n2), cur.next)
            cur = cur.next.next  # move past the inserted node to the next original node
        return head  # return modified list head