# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.dic1={}
        self.dic2=defaultdict(bool)

    def dfs(self,node):
        if node is None:
            return
        if node.left is not None:
            self.dic1[node.left.val]=node
        if node.right is not None:
            self.dic1[node.right.val]=node
        self.dfs(node.left)
        self.dfs(node.right)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dic1[root.val]=None
        self.dfs(root)
        while p is not None:
            self.dic2[p.val]=True
            p=self.dic1[p.val]
        while q is not None:
            if self.dic2[q.val]:
                return q
            q=self.dic1[q.val]
        return None

if __name__ == '__main__':
    sol=Solution()
    node=TreeNode(3)
    node1=TreeNode(5)
    node2=TreeNode(1)
    node.left=node1
    node.right=node2
    print(sol.lowestCommonAncestor(node,node1,node2).val)
