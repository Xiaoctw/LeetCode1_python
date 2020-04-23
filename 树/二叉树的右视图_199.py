# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.dic1 = {}
        self.max_height=-1

    def rightSideView(self, root: TreeNode) -> List[int]:
        if root:
            self.dfs(root,0)
            res=[]
            for i in range(self.max_height+1):
                res.append(self.dic1[i])
            return res
        return []

    def dfs(self,node,height):
        self.max_height=max(self.max_height,height)
        if height not in self.dic1:
            self.dic1[height]=node.val
        if node.right:
            self.dfs(node.right,height+1)
        if node.left:
            self.dfs(node.left,height+1)

