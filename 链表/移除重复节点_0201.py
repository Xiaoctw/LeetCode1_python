# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import *
class Solution:
    '''

    '''
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dic={head.val}
        pos=head
        while pos.next:
            cur=pos.next
            if cur.val not in dic:
                dic.add(cur.val)
                pos=pos.next
            else:
                pos.next=pos.next.next
        return head



if __name__ == '__main__':
    sol=Solution()
    node1=ListNode(1)
    node2=ListNode(1)
    node3=ListNode(1)
    node4=ListNode(1)
    node5=ListNode(2)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    tem=sol.removeDuplicateNodes(node1)
    while tem:
        print(tem.val)
        tem=tem.next
