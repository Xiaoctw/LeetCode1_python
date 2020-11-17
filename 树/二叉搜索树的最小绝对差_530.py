# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        p = root
        stack = []
        res = sys.maxsize
        pre = None
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                if pre:
                    res = min(res, abs(p.val - pre.val))
                pre = p
                p = p.right
        return res
