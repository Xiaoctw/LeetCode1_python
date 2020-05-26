from typing import *
from collections import defaultdict


class Solution:
    '''
    记录和为某个值得下标个数
    '''

    def subarraySum(self, nums: List[int], k: int) -> int:
        dic1 = defaultdict(int)
        dic1[0] = 1
        cnt = 0
        sum = 0
        for val in nums:
            sum += val
            if sum - k in dic1:
                cnt += dic1[sum - k]
            dic1[sum] += 1
        return cnt


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 1, 1]
    print(sol.subarraySum(nums, 2))
