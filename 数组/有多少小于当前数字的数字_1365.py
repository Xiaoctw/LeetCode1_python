from typing import *
import bisect


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list1 = nums[:]
        list1.sort()
        res = []
        for val in nums:
            res.append(bisect.bisect_left(list1, val))
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [7, 7, 7, 7]
    print(sol.smallerNumbersThanCurrent(nums))
