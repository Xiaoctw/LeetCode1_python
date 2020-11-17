# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        p = root
        res = []
        while p or stack:
            if p:
                stack.append(p)
                res.append(p.val)
                p = p.left
            else:
                p = stack.pop(-1)
                p = p.right
        return res
