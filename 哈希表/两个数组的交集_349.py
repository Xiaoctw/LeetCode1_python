from typing import *


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        res = set()
        for val in nums2:
            if val in set1:
                res.add(val)
        return list(res)
