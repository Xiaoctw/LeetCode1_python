# Definition for a binary tree node.
from typing import *
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        que = deque([])
        que.append(root)
        flag = True
        while que:
            l = len(que)
            tem_list = []
            for _ in range(l):
                node = que.popleft()
                tem_list.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if flag:
                ans.append(tem_list)
                flag = False
            else:
                ans.append(tem_list[::-1])
                flag = True
        return ans
