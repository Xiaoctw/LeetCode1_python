# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack=[]
        p=root
        list1=[]
        while stack or p:
            if p:
                stack.append(p)
                list1.append(p)
                p=p.left
            else:
                p=stack.pop()
                p=p.right
        for i in range(1,len(list1)):
            list1[i-1].right=list1[i]
            list1[i-1].left=None

if __name__ == '__main__':
    sol=Solution()
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(5)
    node4=TreeNode(3)
    node5=TreeNode(4)
    node6=TreeNode(6)
    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.right=node5
    node3.right=node6
    sol.flatten(node1)
    p=node1
    while p:
        print(p.val)
        p=p.right
