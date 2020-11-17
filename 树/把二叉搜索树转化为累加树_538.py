# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        p = root
        stack = deque([])
        tem_sum = 0
        while stack or p:
            if p:
                stack.append(p)
                p = p.right
            else:
                p = stack.pop()
                tem_sum += p.val
                p.val=tem_sum
                p = p.left
        return root


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(13)
    print(sol.convertBST(root))
