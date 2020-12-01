# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        level = 0
        node = root
        while node.left:
            node = node.left
            level += 1
        low, hi = 1 << level, (1 << (level + 1)) - 1
        res = low
        while low < hi:
            mid = (hi - low+1) // 2 + low
            if self.exist(root, level, mid):
                res = mid
                low = mid
            else:
                hi = mid - 1
        return res

    def exist(self, root, level, k):
        bits = 1 << (level - 1)
        node = root
        while node is not None and bits > 0:
            if bits & k == 0:
                node = node.left
            else:
                node = node.right
            bits >>= 1
        return node is not None
