from typing import *
import sys
class Solution:

    def splitArray(self, nums: List[int], m: int) -> int:
        lo,hi=-sys.maxsize,0
        for val in nums:
            hi+=val
            lo=max(lo,val)
        res=hi
        while lo<=hi:
            mid=(hi+lo)//2
            if self.check(nums,mid,m):
                hi=mid-1
                res=mid
            else:
                lo=mid+1
        return res

    def check(self,nums,val,m):
        cnt=1
        tem_sum=0
        for i,num in enumerate(nums):
            tem_sum+=num
            if tem_sum>val:
                cnt+=1
                tem_sum=num
    #    print(cnt)
        return cnt<=m


if __name__ == '__main__':
    sol=Solution()
    nums=[7,2,5,10,8]
    m=2
    print(sol.splitArray(nums,2))
