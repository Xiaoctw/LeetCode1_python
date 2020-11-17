# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new_head = ListNode(-1)
        new_head.next = head
        p1, p2 = new_head, new_head
        k = 0
        while k < n:
            p2 = p2.next
            k += 1
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        p1.next = p1.next.next
        return new_head.next


if __name__ == '__main__':
    sol = Solution()
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p = sol.removeNthFromEnd(p1, 5)
    while p:
        print(p.val)
        p = p.next
