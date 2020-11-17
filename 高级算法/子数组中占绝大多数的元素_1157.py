from typing import *
from collections import defaultdict
import bisect


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.idx = defaultdict(list)
        for i, num in enumerate(arr):
            self.idx[num].append(i)
        self.idx = sorted(self.idx.items(), key=lambda x: -len(x[1]))

    def query(self, left: int, right: int, threshold: int) -> int:
        for num, idxs in self.idx:
            if len(idxs) >= threshold:
                l_idx = bisect.bisect_left(idxs, left)
                r_idx = bisect.bisect_right(idxs, right)
                if r_idx - l_idx >= threshold:
                    return num
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
