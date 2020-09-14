# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import *


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                else:
                    res.append(root.val)
                    predecessor.right = None
                    root = root.right
            else:
                res.append(root.val)
                root = root.right
        return res
