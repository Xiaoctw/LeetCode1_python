from typing import *


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 4, 3, 2]
    print(sol.arrayPairSum(nums))
