from typing import *
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp=[1]*len(nums)
        cnts=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    if dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
                        cnts[i]=cnts[j]
                    elif dp[j]+1==dp[i]:
                        cnts[i]+=cnts[j]
        max_len=max(dp)
        res=0
        for i in range(len(dp)):
            if dp[i]==max_len:
                res+=cnts[i]
        return res

if __name__ == '__main__':
    sol=Solution()
    print(sol.findNumberOfLIS([2,2,2,2,2]))


