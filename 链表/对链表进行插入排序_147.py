# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)
        node = head
        while node:
            next_node = node.next
            tem = new_head
            while tem.next and tem.next.val < node.val:
                tem = tem.next
            node.next = tem.next
            tem.next = node
            node = next_node
        return new_head.next


if __name__ == '__main__':
    sol = Solution()
    node1 = ListNode(-1)
    node2 = ListNode(5)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(0)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    tem = sol.insertionSortList(node1)
    while tem:
        print(tem.val)
        tem = tem.next
