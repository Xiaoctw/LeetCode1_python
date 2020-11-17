# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import *
from collections import defaultdict


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        stack = []
        cnts = defaultdict(int)
        p = root
        max_val = -1
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                cnts[p.val] += 1
                max_val = max(max_val, cnts[p.val])
                p = p.right
        val_list = []
        for val in cnts:
            if cnts[val] == max_val:
                val_list.append(val)
        return val_list


if __name__ == '__main__':
    sol = Solution()
    root1 = TreeNode(1)
    root1.left = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    root1.right = node1
    node1.left = node2
    print(sol.findMode(root1))
