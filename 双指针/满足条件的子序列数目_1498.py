from typing import *
import sys


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = int(10 ** 9 + 7)
        nums.sort()
        # 便于计算
        pows = [1]
        for _ in range(len(nums)):
            pows.append(2 * pows[-1] % mod)
        i = 0
        ans = 0
        j = len(nums) - 1
        while True:
            '''
            每次循环得到的是以i开头的，长度不固定满足条件子序列个数
            '''
            if i >= len(nums) or 2 * nums[i] > target:
                break
            while j > i and nums[i] + nums[j] > target:
                j -= 1
            ans = (ans % mod + int(pows[j - i]) % mod) % mod
            i += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [7, 10, 7, 3, 7, 5, 4]
    target = 12
    print(sol.numSubseq(nums, target))
