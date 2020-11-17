# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from 树.TreeNode import *


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def build(beg1, end1, beg2, end2):
            """
            :type beg1 int
            :type beg2 int
            :type end1 int
            :type end2 int
            :return:
            """
            if beg1 > end1:
                return None
            val = postorder[end2]
            root = TreeNode(val)
            index = 0
            for i in range(beg1, end1 + 1):
                if inorder[i] == val:
                    index = i
                    break
            root.left = build(beg1, index - 1, beg2, beg2 + index - beg1 - 1)
            root.right = build(index + 1, end1, beg2 - beg1 + index, end2 - 1)
            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = Solution().buildTree(inorder, postorder)
    print(root.left.val)
    print(root.right.val)
