# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        que = deque([])
        que.append(root)
        while que:
            len_que = len(que)
            pre_node = None
            for i in range(len_que):
                tem_node = que.popleft()
                if pre_node:
                    pre_node.next = tem_node
                    pre_node = tem_node
                else:
                    pre_node = tem_node
                if tem_node.left:
                    que.append(tem_node.left)
                if tem_node.right:
                    que.append(tem_node.right)
        return root
