from typing import *
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node2idx1={}
        idx2node1={}
        tem=head
        idx=0
        while tem is not None:
            node2idx1[tem]=idx
            idx2node1[idx]=tem
            tem=tem.next
            idx+=1

        randomdic={}
        tem=head
        while tem is not None:
            if tem.random is not None:
                randomdic[node2idx1[tem]]=node2idx1[tem.random]
            tem=tem.next

        node2idx2={}
        idx2node2={}
        new_head=Node(-1)
        tem1=new_head
        tem2=head
        idx=0
        while tem2 is not None:
            tem1.next=Node(tem2.val)
            tem1=tem1.next
            tem2=tem2.next
            node2idx2[tem1]=idx
            idx2node2[idx]=tem1
            idx+=1

        tem=new_head.next
        while tem is not None:
            idx=node2idx2[tem]
            if idx in randomdic:
                tem.random=idx2node2[randomdic[idx]]
            tem=tem.next

        return new_head.next




