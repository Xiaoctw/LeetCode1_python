# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        next_head = head.next.next
        p1, p2 = head, head.next
        p2.next = p1
        p1.next = self.swapPairs(next_head)
        return p2

if __name__ == '__main__':
    sol=Solution()
    p1=ListNode(1)
    p2=ListNode(2)
    p3=ListNode(3)
    p4=ListNode(4)
    p5=ListNode(5)
    p1.next=p2
    p2.next=p3
    p3.next=p4
    p4.next=p5
    head=sol.swapPairs(p1)
    while head:
        print(head.val)
        head=head.next
