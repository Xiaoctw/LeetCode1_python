# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.judge(root1, root2)

    def judge(self, node1, node2):
        if (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
            return False
        if node2 is None and node1 is None:
            return True
        if node2.val != node1.val:
            return False
        return (self.judge(node1.left, node2.left) and self.judge(node1.right, node2.right)) \
               or (self.judge(node1.right, node2.left) and self.judge(node1.left, node2.right))
