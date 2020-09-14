# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import *
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        que = deque([])
        res = []
        que.append(root)
        while que:
            size = len(que)
            tem_sum = 0
            for i in range(size):
                node = que.popleft()
                # print(node.val)
                tem_sum += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(tem_sum / size)
        return res


if __name__ == '__main__':
    sol = Solution()
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node1.left = node2
    node1.right = node3
    print(sol.averageOfLevels(node1))
