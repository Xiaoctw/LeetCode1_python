from typing import *


class Solution:
    """
    本题不要直接排序，采用桶排序的方法解决
    """
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        list1=[[] for _ in range(R+C)]
        for r in range(R):
            for c in range(C):
                list1[abs(r-r0)+abs(c-c0)].append([r,c])
        res=[]
        for i in range(R+C):
            res.extend(list1[i])
        return res




