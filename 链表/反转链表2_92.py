# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        newHead=ListNode(0)
        newHead.next=head
        tem1,tem2=newHead,newHead
        k=0
        while k<n-m:
            tem1=tem1.next
            k+=1
        pre=tem2
        k=0
        while k<m:
            if k<m-1:
                pre=pre.next
            tem2=tem2.next
            tem1=tem1.next
            k+=1
        next_head=tem1.next
        tem1.next=None
        pre.next=None
        tail1=tem2
        while tem2:
            tem3=tem2
            tem2=tem2.next
            tem3.next=pre.next
            pre.next=tem3
        tail1.next=next_head
        return newHead.next

if __name__ == '__main__':
    sol=Solution()
    node1=ListNode(1)
    node2=ListNode(2)
    node3=ListNode(3)
    node4=ListNode(4)
    node5=ListNode(5)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    head=sol.reverseBetween(node1,4,5)
    tem=head
    while tem:
        print(tem.val)
        tem=tem.next