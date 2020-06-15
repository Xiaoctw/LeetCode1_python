from typing import *
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[]
        for val in nums:
            if not dp or dp[-1]<val:
                dp.append(val)
            else:
                idx=self.search(dp,0,len(dp)-1,val)
                dp[idx]=val
        return len(dp)

    def search(self,dp,lo,hi,val):
        idx=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if dp[mid]==val:
                return mid
            elif dp[mid]>val:
                idx=mid
                hi=mid-1
            else:
                lo=mid+1
        return idx

if __name__ == '__main__':
    sol=Solution()
    nums=[10,9,2,5,3,7,101,18]
    print(sol.lengthOfLIS(nums))