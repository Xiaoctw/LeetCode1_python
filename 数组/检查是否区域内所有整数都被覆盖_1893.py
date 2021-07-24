from typing import *
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for range in ranges:
            if range[0]<=left and range[1]>=left:
                left=range[1]+1
        return left>right



