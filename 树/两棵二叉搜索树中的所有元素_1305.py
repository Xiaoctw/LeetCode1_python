# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self,node,list1):
        if node:
            list1.append(node.val)
            self.dfs(node.left,list1)
            self.dfs(node.right,list1)
        return list1

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1=self.dfs(root1,[])
        list2=self.dfs(root2,[])
        list1.extend(list2)
        list1.sort()
        return list1

if __name__ == '__main__':
    sol=Solution()
    node1=TreeNode(2)
    node2=TreeNode(1)
    node3=TreeNode(4)
    node1.left=node2
    node1.right=node3
    node4=TreeNode(1)
    node5=TreeNode(0)
    node6=TreeNode(3)
    node4.left=node5
    node4.right=node6
    list1=sol.getAllElements(node1,node4)
    print(list1)
