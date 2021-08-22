# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res=[]
        self.find_path=None
        self.tem_path=[]
        self.find_set=set()

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.find(root,target)
        for i in range(len(self.find_path)-1,max(len(self.find_path)-k-1,-1),-1):
            depth=k-(len(self.find_path)-i)+1
            self.dfs(self.find_path[i],depth)
        return self.res

    def find(self,node,target):
        if node is None or self.find_path is not None:
            return
        if node==target:
            self.tem_path.append(node)
            self.find_path=self.tem_path[:]
            self.tem_path.pop()
            return
        self.tem_path.append(node)
        self.find(node.left,target)
        self.find(node.right,target)
        self.tem_path.pop()

    def dfs(self,node,i):
        if node is None:
            return
        if node.val in self.find_set:
            return
        if i==0 and node.val not in self.res:
            self.res.append(node.val)
        self.dfs(node.left,i-1)
        self.dfs(node.right,i-1)
        self.find_set.add(node.val)

if __name__ == '__main__':
    root=TreeNode(3)
    node1=TreeNode(5)
    node2=TreeNode(1)
    root.left=node1
    root.right=node2
    node3=TreeNode(6)
    node4=TreeNode(2)
    node1.left = node3
    node1.right=node4
    node5=TreeNode(7)
    node6=TreeNode(4)
    node4.left=node5
    node4.right=node6
    node7=TreeNode(0)
    node8=TreeNode(8)
    node2.left=node7
    node2.right=node8
    sol=Solution()
    print(sol.distanceK(root,node1,2))





