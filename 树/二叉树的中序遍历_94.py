# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]; p=root;res=[]
        while (p or len(stack)!=0 ):
            if p:
                stack.append(p)
                p=p.left
            else:
                p=stack.pop(-1)
                res.append(p.val)
                p=p.right
        return res

