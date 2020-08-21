# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        ans = []

        # Return distance from node to target if exists, else -1
        # Vertex distance: the # of vertices on the path from node to target
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                L, R = dfs(node.left), dfs(node.right)
                if L != -1:
                    if L == K: ans.append(node.val)
                    subtree_add(node.right, L + 1)
                    return L + 1
                elif R != -1:
                    if R == K: ans.append(node.val)
                    subtree_add(node.left, R + 1)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                ans.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return ans


if __name__ == '__main__':
    sol = Solution()
    node1 = TreeNode(3)
    node2 = TreeNode(5)
    node3 = TreeNode(1)
    node1.left = node2
    node1.right = node3
    node4 = TreeNode(6)
    node5 = TreeNode(2)
    node2.left = node4
    node2.right = node5
    node6 = TreeNode(7)
    node7 = TreeNode(4)
    node5.left = node6
    node5.right = node7
    node8 = TreeNode(0)
    node9 = TreeNode(8)
    node3.left = node8
    node3.right = node9
    print(sol.distanceK(node1, node2, 2))
