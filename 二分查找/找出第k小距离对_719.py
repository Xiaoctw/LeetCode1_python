from typing import *
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        lo,hi=0,nums[-1]-nums[0]
        while lo<=hi:
            mid=lo+(hi-lo)//2
            num=self.helper(nums,mid)
            if num>=k:
                hi=mid-1
            else:
                lo=mid+1
        return lo


    def helper(self,nums,val):
        '''
        距离小于等于val的对个数
        :param nums:
        :param val:
        :return:
        '''
        i=0
        j=1
        cnt=0
        while j<len(nums):
            while j<len(nums) and nums[j]-nums[i]<=val:
                j+=1
                cnt+=(j-i-1)
            i+=1
        return cnt

if __name__ == '__main__':
    sol=Solution()
    nums=[1,6,1]
    k=3
    print(sol.smallestDistancePair(nums,k))

