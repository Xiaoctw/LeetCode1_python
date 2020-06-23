# Definition for a binary tree node.
import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.max_val=-sys.maxsize

    def maxPathSum(self, root: TreeNode) -> int:
        self.helper1(root)
        return self.max_val

    def helper1(self,node):
        if node is None:
            return -sys.maxsize
        path1=self.helper1(node.left)
        path2=self.helper1(node.right)
        self.max_val=max(self.max_val,node.val,node.val+path1,node.val+path2,node.val+path2+path1)
        return max(node.val,node.val+path2,node.val+path1)


if __name__ == '__main__':
    sol=Solution()
    node1=TreeNode(-3)
    # node2=TreeNode(2)
    # node1.left=node2
    print(sol.maxPathSum(node1))
