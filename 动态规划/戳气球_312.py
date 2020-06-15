from typing import *
import sys
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        len1 = len(nums)
        nums=[1]+nums+[1]
        dp=[[0]*(len1+2) for _ in  range(len1+2)]
        for l in range(1,len1+1):
            for i in range(1,len1-l+2):
                j=i+l-1
                if i==j:
                    dp[i][j]=nums[i-1]*nums[i]*nums[i+1]
                else:
                    dp[i][j]=-sys.maxsize
                    for k in range(i,j+1):
                        if k==i:
                            dp[i][j]=max(dp[i][j],dp[k+1][j]+nums[i-1]*nums[j+1]*nums[k])
                        elif k==j:
                            dp[i][j]=max(dp[i][j],dp[i][k-1]+nums[i-1]*nums[j+1]*nums[k])
                        else:
                            dp[i][j]=max(dp[i][j],dp[k+1][j]+dp[i][k-1]+nums[i-1]*nums[k]*nums[j+1])

        return dp[1][len1]

if __name__ == '__main__':
    sol=Solution()
    print(sol.maxCoins([3,1,5,8]))
