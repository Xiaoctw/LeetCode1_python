from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        val = 0
        for num in nums:
            val = val ^ num
        lowbit = val & (-val)
        val1 = 0
        for num in nums:
            if num & lowbit:
                val1 = val1 ^ num
        return [val1, val1 ^ val]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 4, 4, 5, 6, 5, 6, 7, 7, 8, 8]
    print(sol.singleNumber(nums))
