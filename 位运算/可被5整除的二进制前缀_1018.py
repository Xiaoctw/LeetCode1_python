from typing import *


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        val = 0
        ans = []
        for a in A:
            #在这里有一个整除的话算法效率会高很多
            val = (val * 2)%5 + a
            if val % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
