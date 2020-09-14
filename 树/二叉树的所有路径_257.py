# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import *
class Solution:
    def __init__(self):
        self.res=[]

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.back([],root)
        return self.res


    def back(self,list1,node):
        if node is None:
            return
        list1.append(str(node.val))
        if node.left is None and node.right is None:
            self.res.append('->'.join(list1[:]))
        if node.left is not None:
            self.back(list1,node.left)
        if node.right is not None:
            self.back(list1,node.right)
        list1.pop()

