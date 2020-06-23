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
        tem=head#遍历链表
        res=[]#结果保存在这里
        data=[]#将链表中的元素放到索引数组分钟
        while tem:
            data.append(tem.val)
            res.append(0)
            while que and data[que[-1]]<tem.val:
                idx=que.pop()
                res[idx]=tem.val
            que.append(len(data)-1)
            tem=tem.next
        return res


if __name__ == '__main__':
    sol=Solution()
    node1=ListNode(2)
    node2=ListNode(7)
    node3=ListNode(4)
    node4=ListNode(3)
    node5=ListNode(5)
    # node6=ListNode(2)
    # node7=ListNode(5)
    # node8=ListNode(1)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    # node5.next=node6
    # node6.next=node7
    # node7.next=node8
    print(sol.nextLargerNodes(node1))