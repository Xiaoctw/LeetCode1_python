# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        maxL=0

        def getMaxL(node, val):
            #nonlocal用于在函数或其他作用于最后在那个使用外层（非全局）变量
            nonlocal maxL
            if node==None:
                return 0
            left=getMaxL(node.left,node.val)
            right=getMaxL(node.right,node.val)
            #maxL=max(maxL,left+right)
            if left+right> maxL:
                maxL=left+right
            if node.val==val:
                return max(left,right)+1
            return 0

        if root!=None:
            getMaxL(root,root.val)
        return maxL

