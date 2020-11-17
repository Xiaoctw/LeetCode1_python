# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head, even_head = ListNode(), ListNode()
        flag = 1
        tem = head
        odd_tem, tem_even = odd_head, even_head
        while tem:
            if flag:
                odd_tem.next = tem
                tem = tem.next
                odd_tem = odd_tem.next
                odd_tem.next = None
            else:
                tem_even.next = tem
                tem = tem.next
                tem_even = tem_even.next
                tem_even.next = None
            flag = 1 ^ flag
        odd_tem.next = even_head.next

        return odd_head.next


if __name__ == '__main__':
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    tem = sol.oddEvenList(node1)
    while tem:
        print(tem.val)
        tem = tem.next

    中文 = 'Chinese'
    print(中文)