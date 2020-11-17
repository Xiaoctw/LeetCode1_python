# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys

class Solution:
    """
    三种状态
    0：无摄像头，没有被覆盖，子树被覆盖
    1：无摄像头，被覆盖
    2：有摄像头
    """

    def solve(self, node):
        if not node:
            return 0, 0, sys.maxsize
        l = self.solve(node.left)
        r = self.solve(node.right)
        dp0 = l[1] + r[1]
        dp1 = min(l[2] + min(r[1:]), r[2] + min(l[1:]))
        #可能从父节点处覆盖子节点，因此子节点没有被覆盖的情况也要考虑
        dp2 = 1 + min(l) + min(r)
        return dp0, dp1, dp2

    def minCameraCover(self, root: TreeNode) -> int:
        return min(self.solve(root)[1:])
