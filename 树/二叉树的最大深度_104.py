# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution:
    def __init__(self):
        self.max_depth=0
    def maxDepth(self, root: TreeNode) -> int:
        self.dfs(root,1)
        return self.max_depth
    def dfs(self,node,depth):
        if node is None:
            return
        self.max_depth=max(self.max_depth,depth)
        self.dfs(node.left,depth+1)
        self.dfs(node.right,depth+1)