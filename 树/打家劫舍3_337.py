# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))

    def dfs(self, node):
        if node is None:
            return 0, 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        selected = node.val + l[1] + r[1]
        notselected = max(l) + max(r)
        return selected, notselected
