# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1, p2 = head, head
        while p2:
            if p2.next is None:
                return False
            p2 = p2.next.next
            p1 = p1.next
            if p1 == p2:
                return True
        return False
