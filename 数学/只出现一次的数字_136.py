from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for val in nums:
            res=res^val
        return res

if __name__ == '__main__':
    sol=Solution()
    nums=[2,2,1]
    print(sol.singleNumber(nums))