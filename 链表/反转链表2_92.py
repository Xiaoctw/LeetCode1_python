# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        new_head=ListNode(-1)
        new_head.next=head
        tem=new_head
        k=0
        while k<m-1:
            tem=tem.next
            k+=1
        p1=tem.next
        tem.next=None
        tail=tem
        tem=p1
        k=0
        while k<n-m+1:
            p=tem
            tem=tem.next
            p.next=tail.next
            tail.next=p
            k+=1
        p1.next=tem
        return new_head.next



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
    head=sol.reverseBetween(node1,2,5)
    tem=head
    while tem:
        print(tem.val)
        tem=tem.next