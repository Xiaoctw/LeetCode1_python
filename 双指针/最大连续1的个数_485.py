from typing import *


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                j = i + 1
                while j < len(nums) and nums[j] == 1:
                    j += 1
                max_len = max(max_len, j - i)
                i = j
            else:
                i += 1
        return max_len


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 1, 1, 0, 2, 1, 1, 1]
    print(sol.findMaxConsecutiveOnes(nums))
