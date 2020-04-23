# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        _len = len(preorder)
        return self.build(preorder, inorder, 0, _len - 1, 0, _len - 1)

    def build(self, preorder, inorder, beg1, end1, beg2, end2):
        if beg1 > end1:
            return None
        val = preorder[beg1]
        idx = -1
        for i in range(beg2, end2 + 1):
            if inorder[i] == val:
                idx = i
                break
        root = TreeNode(val)
        root.left = self.build(preorder, inorder, beg1 + 1, idx - beg2 + beg1, beg2, idx - 1)
        root.right = self.build(preorder, inorder, idx - beg2 + beg1 + 1, end1, idx + 1, end2)
        return root
