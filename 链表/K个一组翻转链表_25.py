# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        return self.reverse(head, k)

    def reverse(self, node, k):
        cnt = 1
        tem = node
        while cnt < k:
            if tem is None:
                return node
            tem = tem.next
            cnt += 1
        if tem is None:
            return node
        next_head = self.reverse(tem.next, k)
        new_head = ListNode(0)
        tem.next = None
        tem = node
        while tem is not None:
            node1 = tem
            tem = tem.next
            node1.next = new_head.next
            new_head.next = node1
        tem = new_head
        while tem.next is not None:
            tem = tem.next
        tem.next = next_head
        return new_head.next


if __name__ == '__main__':
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    tem = (sol.reverseKGroup(node1, 6))
    while tem:
        print(tem.val)
        tem = tem.next
