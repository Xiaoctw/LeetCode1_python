# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        new_head = slow.next
        slow.next = None
        new_head = self.reverse_list(new_head)
        p1, p2 = head, new_head
        while p1 is not None and p2 is not None:
            tem1, tem2 = p1.next, p2.next
            p1.next = p2
            p2.next = tem1
            p1 = tem1
            p2 = tem2
        return
        # 头插法

    def reverse_list(self, head):
        new_head = ListNode(0)
        temp = head
        while temp is not None:
            pre = temp
            temp = temp.next
            pre.next = new_head.next
            new_head.next = pre
        return new_head.next
