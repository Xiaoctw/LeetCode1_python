from typing import *
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tem=-sys.maxsize
        res=-sys.maxsize
        for i in nums:
            tem=max(i,tem+i)
            res=max(res,tem)
        return res

if __name__ == '__main__':
    sol=Solution()
    nums = [-2, 1]
    print(sol.maxSubArray(nums))
