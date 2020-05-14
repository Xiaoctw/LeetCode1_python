# Definition for a binary tree node.
from typing import *
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        que=deque([])
        que.append(root)
        res=[]
        while que:
            size1=len(que)
            list1=[]
            for _ in range(size1):
                node1=que.popleft()
                list1.append(node1.val)
                if node1.left:
                    que.append(node1.left)
                if node1.right:
                    que.append(node1.right)
            res.append(list1)
        return res

if __name__ == '__main__':
    sol=Solution()
    root=TreeNode(3)
    node1=TreeNode(9)
    node2=TreeNode(20)
    node3=TreeNode(15)
    node4=TreeNode(7)
    root.left=node1
    root.right=node2
    node2.left=node3
    node2.right=node4
    print(sol.levelOrder(root))