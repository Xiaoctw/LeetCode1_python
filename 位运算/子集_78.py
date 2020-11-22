from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for mask in range(1 << n):
            l = []
            for i in range(n):
                if 1 << i & mask:
                    l.append(nums[i])
            res.append(l)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.subsets(nums))
