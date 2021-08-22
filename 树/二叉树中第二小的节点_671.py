# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.min_val=None
        self.ans=-1
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1
        self.min_val=root.val
        self.dfs(root)
        return self.ans

    def dfs(self,node):
        if node is None:
            return
        if node.val>self.min_val:
            if self.ans==-1:
                self.ans=node.val
            else:
                self.ans=min(node.val,self.ans)
            return
        self.dfs(node.left)
        self.dfs(node.right)




