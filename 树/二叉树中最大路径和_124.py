# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from 树.TreeNode import TreeNode
import sys
class Solution:



    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxL=-sys.maxsize
        def maxPath(root):
            """
            仍然是利用全局变量求解值，函数来计算不带弯的极值
            :param root:
            :return:
            """
            nonlocal maxL
            if root==None:
                return 0
            max_left=maxPath(root.left)
            max_right=maxPath(root.right)
            # cur_val=0
            # cur_val=cur_val+max_left if max_left>0 else 0
            # cur_val=cur_val+max_right if max_right>0 else 0
            maxL=max(maxL,max_left+max_right+root.val,max_left+root.val,max_right+root.val,root.val)
            return max(max_left+root.val,max_right+root.val,root.val)
        if root==None:
            return 0
        maxPath(root)
        return maxL

node1=TreeNode(-10)
node2=TreeNode(9)
node3=TreeNode(20)
node4=TreeNode(15)
node5=TreeNode(7)
node1.left=node2
node1.right=node3
node3.left=node4
node3.right=node5
print(Solution().maxPathSum(node1))