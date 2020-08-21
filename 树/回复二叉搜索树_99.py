# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        p = root
        list1 = []
        while (stack or p):
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                list1.append(p.val)
                p = p.right
        #  print(list1)
        idx1, idx2 = -1, -1
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                if idx1 == -1:
                    idx1 = i
                else:
                    idx2 = i + 1
        if idx2 == -1:
            list1[idx1], list1[idx1 + 1] = list1[idx1 + 1], list1[idx1]
        else:
            list1[idx1], list1[idx2] = list1[idx2], list1[idx1]
        p = root
        stack = []
        idx = 0
        while (stack or p):
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                p.val = list1[idx]
                #  print(p.val)
                idx += 1
                p = p.right


if __name__ == '__main__':
    sol = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node1.left = node2
    node2.right = node3
    sol.recoverTree(node1)
