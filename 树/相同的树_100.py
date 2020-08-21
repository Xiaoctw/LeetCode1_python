# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        que1,que2=deque([]),deque([])
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p is None and q is None:
            return True
        que1.append(p)
        que2.append(q)
        while que1:
            node1=que1.popleft()
            node2=que2.popleft()
            if node1.val!=node2.val:
                return False
            if node1.left is None and node2.left is not None:
                return False
            if node1.left is not None and node2.left is None:
                return False
            if node1.left is not None:
                que1.append(node1.left)
                que2.append(node2.left)
            if node1.val!=node2.val:
                return False
            if node1.right is None and node2.right is not None:
                return False
            if node1.right is not None and node2.right is None:
                return False
            if node1.right is not None:
                que1.append(node1.right)
                que2.append(node2.right)
        return True





