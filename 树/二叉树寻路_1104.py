from typing import *
from collections import deque
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        # 先把不是Z字型的父节点算出来，顺序完全二叉树的父节点是 node//2
        # 基于一个归纳，当前节点除以2取整就是父节点的值
        res = []
        while label != 1:
            res.append(label)
            label//=2
        res.append(1)
        res.reverse()
        # 从倒数第二个开始，每隔一个，找出取反相对应的值
        for i in range(len(res)-2, -1, -2):
            original = res[i]
            #
            start = 2**i
            end = 2**(i+1) -1
            new = start + end - original
            res[i] = new

        return res

