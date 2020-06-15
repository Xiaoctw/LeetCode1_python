# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
from collections import  deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root,root)

    def check(self,p,q):
        #每次向队列中放入两个元素
        #两个元素每次判断是否相同
        que=deque([])
        que.append(p)
        que.append(q)
        while que:
            u=que.popleft()
            v=que.popleft()
            if not u and not v:
                continue
            if not u or not v or u.val!=v.val:
                return False
            que.append(u.left)
            que.append(v.right)
            que.append(u.right)
            que.append(v.left)
        return True





if __name__ == '__main__':
    sol=Solution()
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node1.left=node2
    node1.right=node3
    print(sol.isSymmetric(node1))