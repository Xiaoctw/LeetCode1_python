from typing import *
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        lo,hi=1,max(nums)
        ans=hi
        while lo<=hi:
            mid=(hi-lo)//2+lo
            if self.helper(nums,mid)<=threshold:
                ans=min(ans,mid)
                hi=mid-1
            else:
                lo=mid+1
        return ans

    def helper(self,nums,k):
        s=0
        for num in nums:
            s+=math.ceil(num/k)
        return s

if __name__ == '__main__':
    sol=Solution()
    nums = [2,3,5,7,11]
    threshold = 11
    print(sol.smallestDivisor(nums,threshold))


