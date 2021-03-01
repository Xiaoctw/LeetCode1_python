from typing import *
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp=defaultdict(lambda :0)
        pre_set=set()
        pre_set.add(0)
        dp[0,-1]=1
        for i,num in enumerate(nums):
            tem_set=set()
            for val in pre_set:
                dp[val+num,i]+=dp[val,i-1]
                dp[val-num,i]+=dp[val,i-1]
                tem_set.add(val+num)
                tem_set.add(val-num)
            pre_set=tem_set
        return dp[S,len(nums)-1]

if __name__ == '__main__':
    sol=Solution()
    nums=[1,1,1,1,1]
    print(sol.findTargetSumWays(nums,3))
