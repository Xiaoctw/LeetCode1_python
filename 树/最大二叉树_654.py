# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, beg, end):
        if beg > end:
            return None
        max_idx = beg
        for i in range(beg, end + 1):
            if nums[max_idx] < nums[i]:
                max_idx = i
        root = TreeNode(nums[max_idx])
        root.left = self.helper(nums, beg, max_idx - 1)
        root.right = self.helper(nums, max_idx + 1, end)
        return root

def dfs(node):
    if node is None:
        return
    print('{} '.format(node.val))
    dfs(node.left)
    dfs(node.right)



if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    sol=Solution()
    node=sol.constructMaximumBinaryTree(nums)
    dfs(node)