# Definition for a binary tree node.
from typing import *
import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.judge(root)

    def judge(self,node:'TreeNode'):
        if node is None:
            return True
        left_val=self.max_val(node.left)
        right_val=self.min_val(node.right)
        if not (left_val<node.val<right_val):
            return False
        return self.judge(node.left) and self.judge(node.right)

    def min_val(self,node:'TreeNode'):
        if node is None:
            return sys.maxsize
        val=min(self.min_val(node.left),self.min_val(node.right),node.val)
        return val

    def max_val(self,node):
        if node is None:
            return -sys.maxsize
        val=max(self.max_val(node.left),self.max_val(node.right),node.val)
        return val

if __name__ == '__main__':
    sol=Solution()
    node1=TreeNode(2)
    node2=TreeNode(1)
    node3=TreeNode(3)
    node1.left=node2
    node1.right=node3
    print(sol.isValidBST(node1))