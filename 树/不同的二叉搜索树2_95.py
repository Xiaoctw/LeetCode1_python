# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import *
class Solution:
    def __init__(self):
        self.dic={}

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        return self.helper(1,n)

    def helper(self,beg,end):
        if beg>end:
            return [None]
        if (beg,end) in self.dic:
            return self.dic[beg,end]
        if beg==end:
            node=TreeNode(beg)
            self.dic[beg,end]=[node]
            return self.dic[beg,end]
        l = []
        for k in range(beg,end+1):
            list1=self.helper(beg,k-1)
            list2=self.helper(k+1,end)
            for node1 in list1:
                for node2 in list2:
                    node=TreeNode(k)
                    node.left=node1
                    node.right=node2
                    l.append(node)
        self.dic[beg,end]=l
        return l

if __name__ == '__main__':
    sol=Solution()
    print(len(sol.generateTrees(3)))
