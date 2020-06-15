# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution:
    '''
    三种状态
    0:
    '''
    def solve(self,node):
        if not node:
            return 0,0,sys.maxsize
        l=self.solve(node.left)
        r=self.solve(node.right)
        dp0=l[1]+r[1]
        dp1=min(l[2]+min(r[1:]),r[2]+min(l[1:]))
        dp2=1+min(l)+min(r)
        return dp0,dp1,dp2


    def minCameraCover(self, root: TreeNode) -> int:
        return min(self.solve(root)[1:])