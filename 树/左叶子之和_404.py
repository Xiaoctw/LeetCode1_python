# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    计算所有左叶子之和
    """

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.dfs(root, False)

    def dfs(self, node, from_left):
        if node is None:
            return 0
        if from_left and node.left is None and node.right is None:
            return node.val
        return sum([self.dfs(node.left, True), self.dfs(node.right, False)])
