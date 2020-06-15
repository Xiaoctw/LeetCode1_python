# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import *
from collections import deque
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d==1:
            new_root=TreeNode(v)
            new_root.left=root
            return new_root
        que=deque([])
        que.append(root)
        heads=[]
        cnt=1
        while que:
            len1=len(que)
            cnt+=1
            heads=[]
            for i in range(len1):
                heads.append(que.popleft())
            if cnt==d:
                break
            for node in heads:
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        for head in heads:
            l,r=head.left,head.right
            head.left,head.right=TreeNode(v),TreeNode(v)
            head.left.left=l
            head.right.right=r
        return root

if __name__ == '__main__':
    sol=Solution()
    node1=TreeNode(4)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node4=TreeNode(1)
    node1.left=node2
    node2.left=node3
    node2.right=node4
    sol.addOneRow(node1,1,3)
