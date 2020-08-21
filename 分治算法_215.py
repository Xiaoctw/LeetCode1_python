import random
from typing import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.helper2(nums, 0, len(nums) - 1, len(nums) - k + 1)

    def helper2(self, nums, lo, hi, k):
        '''

        :param nums:
        :param lo:
        :param hi:
        :param k:
        :return:
        '''
        idx = self.helper1(nums, lo, hi)
        if idx - lo + 1 == k:
            return nums[idx]
        elif idx - lo + 1 > k:
            return self.helper2(nums, lo, idx - 1, k)
        return self.helper2(nums, idx + 1, hi, k - idx + lo - 1)

    def helper1(self, nums, lo, hi):
        # 返回的是找到目标的idx
        idx = random.randint(lo, hi)
        nums[idx], nums[hi] = nums[hi], nums[idx]
        val = nums[hi]
        i = lo - 1
        for j in range(lo, hi):
            if nums[j] < val:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[hi] = nums[hi], nums[i + 1]
        return i + 1


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sol.findKthLargest(nums, 9))
# print(nums)
