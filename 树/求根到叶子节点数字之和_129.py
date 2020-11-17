# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.sum

    def dfs(self, node, val):
        if not node:
            return
        val = val * 10 + node.val
        if node.left is None and node.right is None:
            self.sum += val
        self.dfs(node.left, val)
        self.dfs(node.right, val)
