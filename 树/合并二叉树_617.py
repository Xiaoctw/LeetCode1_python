# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.dfs(t1, t2)

    def dfs(self, root1, root2):
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            new_root = TreeNode(root2.val)
            new_root.left = self.dfs(None, root2.left)
            new_root.right = self.dfs(None, root2.right)
        elif root2 is None:
            new_root = TreeNode(root1.val)
            new_root.left = self.dfs(root1.left, None)
            new_root.right = self.dfs(root1.right, None)
        else:
            new_root = TreeNode(root1.val + root2.val)
            new_root.left = self.dfs(root1.left, root2.left)
            new_root.right = self.dfs(root1.right, root2.right)
        return new_root
