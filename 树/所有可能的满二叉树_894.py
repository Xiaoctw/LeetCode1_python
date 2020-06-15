# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import *
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N%2==0:
            return []
        if N==1:
            return [TreeNode(0)]
        res = []
        for i in range(1,N,2):
            left_list=self.allPossibleFBT(i)
            right_list=self.allPossibleFBT(N-1-i)
            for node1 in left_list:
                for node2 in right_list:
                    root=TreeNode(0)
                    root.left=node1
                    root.right=node2
                    res.append(root)
        return res

if __name__ == '__main__':
    sol=Solution()
    node_list=sol.allPossibleFBT(7)
    print()