# Definition for singly-linked list.
from typing import *
from collections import deque
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        que=deque([])
        tem=head
        while tem:
            while que and que[-1]<tem.val:
                que.pop()
            que.append(tem.val)
            tem=tem.next
        tem=head
        res=[]
        while tem:
            if tem.val==que[0]:
                que.popleft()
            if que:
                if que[0]<=tem.val:
                    res.append(0)
                else:
                    res.append(que[0])
            else:
                res.append(0)
            tem=tem.next
        return res

if __name__ == '__main__':
    sol=Solution()
    node1=ListNode(1)
    node2=ListNode(7)
    node3=ListNode(5)
    node4=ListNode(1)
    node5=ListNode(9)
    node6=ListNode(2)
    node7=ListNode(5)
    node8=ListNode(1)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    node5.next=node6
    node6.next=node7
    node7.next=node8
    print(sol.nextLargerNodes(node1))