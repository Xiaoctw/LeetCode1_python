from typing import *
from collections import defaultdict


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        dics = [defaultdict(int) for _ in range(len(A))]
        set1 = set()
        for (i, s) in enumerate(A):
            for c in s:
                dics[i][c] += 1
                set1.add(c)
        res = []
        for c in set1:
            min_cnt = min([dics[i][c] for i in range(len(A))])
            res.extend([c]*min_cnt)
        return res

if __name__ == '__main__':
    sol=Solution()
    strs=["bella", "label", "roller"]
    print(sol.commonChars(strs))

