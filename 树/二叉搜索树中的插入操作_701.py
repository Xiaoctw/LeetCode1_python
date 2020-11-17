# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if root.val<val:
            root.right=self.insertIntoBST(root.right,val)
        else:
            root.left=self.insertIntoBST(root.left,val)
        return root


if __name__ == '__main__':
    sol=Solution()
    root=TreeNode(4)
    node1=TreeNode(2)
    node2=TreeNode(7)
    node3=TreeNode(1)
    node4=TreeNode(3)
    root.left=node1
    root.right=node2
    node1.left=node3
    node1.right=node4
    sol.insertIntoBST(root,0)
    print()