# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums,0,len(nums)-1)

    def helper(self,nums,i,j):
        if i>j:
            return None
        k=(i+j)//2
        node1=TreeNode(nums[k])
        node1.left=self.helper(nums,i,k-1)
        node1.right=self.helper(nums,k+1,j)
        return node1

if __name__ == '__main__':
    sol=Solution()
    nums=[-10,-3,0,5,9]
    root=sol.sortedArrayToBST(nums)
    print()