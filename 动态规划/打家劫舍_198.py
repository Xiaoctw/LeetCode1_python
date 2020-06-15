from typing import *
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]

if __name__ == '__main__':
    sol=Solution()
    print(sol.rob([1,2,3,1,4,3,5,4,3,2,4,5,5,7,8,9]))