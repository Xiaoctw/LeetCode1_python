# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head=ListNode(0)
        tem=new_head
        tem1,tem2=l1,l2
        while tem1 and tem2:
            if tem1.val<tem2.val:
                tem.next=ListNode(tem1.val)
                tem1=tem1.next
                tem=tem.next
            else:
                tem.next=ListNode(tem2.val)
                tem2=tem2.next
                tem=tem.next
        while tem1:
            tem.next=tem1
            tem=tem1
            tem1=tem1.next
        while tem2:
            tem.next=tem2
            tem=tem2
            tem2=tem2.next
        return new_head.next

if __name__ == '__main__':
    sol=Solution()
    node1=ListNode(1)
    node2=ListNode(2)
    node3=ListNode(3)
    node1.next=node2
    node2.next=node3
    node4=ListNode(1)
    node5=ListNode(3)
    node6=ListNode(4)
    node4.next=node5
    node5.next=node6
    sol=Solution()
    new_head=sol.mergeTwoLists(node1,node4)
    tem=new_head
    while tem:
        print(tem.val)
        tem=tem.next


