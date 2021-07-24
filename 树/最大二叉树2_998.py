# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
            if root is None or val>root.val:
                node=TreeNode(val)
                node.left=root
                return node
            head=self.insertIntoMaxTree(root.right,val)
            root.right=head
            return root