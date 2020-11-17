# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import *
from collections import deque


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, stack = [], []
        prev = None
        while root or stack:
            while root:  # 一直找到最左端的节点
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                # 在这里访问该节点，条件是没有右子树，或者是右子节点已经被访问了
                res.append(root.val)
                prev = root
                root = None
            else:
                # 说明现在还不需要访问该节点，先去访问右子树
                stack.append(root)
                root = root.right
        return res


if __name__ == '__main__':
    sol = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    print(sol.postorderTraversal(node1))
