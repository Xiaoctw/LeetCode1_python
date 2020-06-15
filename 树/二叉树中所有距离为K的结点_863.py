# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.dic1 = {}
        self.dic2 = {}
        self.res = []

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root:
            return []
        self.dfs(root, None)
        self.find_node(target, K)
        tem = target
        for i in range(1, K + 1):
            if i == K:
                pre = self.dic1[tem.val]
                if pre:
                    self.res.append(pre.val)
                else:
                    break
            else:
                pre = self.dic1[tem.val]
                if pre:
                    if self.dic2[tem.val]:
                        self.find_node(pre.right, K - i - 1)
                    else:
                        self.find_node(pre.left, K - i - 1)
                else:
                    break
            tem = pre
        return self.res

    def dfs(self, node1, pre):
        if pre:
            self.dic1[node1.val] = pre
            if pre.left and pre.left.val == node1.val:
                self.dic2[node1.val] = True
            else:
                self.dic2[node1.val] = False
        else:
            self.dic1[node1.val]=None
        if node1.left:
            self.dfs(node1.left, node1)
        if node1.right:
            self.dfs(node1.right, node1)

    def find_node(self, root, K):
        '''
        在root为根节点的子树上寻找深度为K的结点
        :param root:
        :param K:
        :return:
        '''
        if K == 0:
            self.res.append(root.val)
        if root.left:
            self.find_node(root.left, K - 1)
        if root.right:
            self.find_node(root.right, K - 1)


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
