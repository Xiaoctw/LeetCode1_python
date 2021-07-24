# Definition for a binary tree node.
from typing import *
import bisect


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.tem_res = None
        self.chars = 'abcdefghijklmnopqrstuvwxyz'

    def smallestFromLeaf(self, root: TreeNode) -> str:
        if root is None:
            return ''
        self.dfs(root, '')
        return self.tem_res

    def dfs(self, node, s):
        if node is None:
            return
        s= self.chars[node.val] + s
        if node.left is None and node.right is None:
            if self.tem_res is None or s < self.tem_res:
                self.tem_res = s
        self.dfs(node.left, s)
        self.dfs(node.right, s)


if __name__ == '__main__':
    sol = Solution()
