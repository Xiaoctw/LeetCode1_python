# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import *
class Solution:
    def __init__(self):
        self.res=False
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.helper(root,sum)
        return self.res

    def helper(self,node,sum):
        if node is None or self.res:
            return
        if node.val ==sum and node.left is None and node.right is None:
            self.res=True
            return
        if node.left:
            self.helper(node.left,sum-node.val)
        if node.right:
            self.helper(node.right,sum-node.val)

