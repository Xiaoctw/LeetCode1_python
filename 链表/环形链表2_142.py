# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        p1,p2=head,head
        while p2:
            if p2.next is None:
                return None
            p2=p2.next.next
            p1=p1.next
            if p2==p1:
                break
        p1=head
        if p2 is None:
            return None
        while p1!=p2:
            p1=p1.next
            p2=p2.next
        return p2
