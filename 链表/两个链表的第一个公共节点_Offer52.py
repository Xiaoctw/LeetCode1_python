# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len1=0
        len2=0
        tem=headA
        while tem is not None:
            tem=tem.next
            len1+=1
        tem=headB
        while tem is not None:
            tem=tem.next
            len2+=1
        i=0
        tem1,tem2=headA,headB
        if len2>len1:
            while i<len2-len1:
                tem2=tem2.next
                i+=1
        if len1>len2:
            while i<len1-len2:
                tem1=tem1.next
                i+=1
        while tem1 is not None and tem2 is not None and tem2!=tem1:
            tem1=tem1.next
            tem2=tem2.next
        return tem1


