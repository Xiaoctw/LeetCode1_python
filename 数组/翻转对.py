from typing import *
import bisect
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.merge(nums,0,len(nums)-1)

    def merge(self,nums,lo,hi):
        if lo>=hi:
            return 0
        mid=(lo+hi)//2
        num1=self.merge(nums,lo,mid)
        num2=self.merge(nums,mid+1,hi)
        cnt=0
        for i in range(mid,lo-1,-1):
            val1=nums[i]
            idx=bisect.bisect_left(nums,val1/2,lo=mid+1,hi=hi+1)
            cnt+=(idx-mid-1)
            if idx==mid+1:
                break
        arr=[0]*(hi-lo+1)
        i,j,k=lo,mid+1,0
        while i<=mid and j<=hi:
            if nums[i]<nums[j]:
                arr[k]=nums[i]
                i+=1
            else:
                arr[k]=nums[j]
                j+=1
            k+=1
        while i<=mid:
            arr[k]=nums[i]
            k+=1
            i+=1
        while j<=hi:
            arr[k]=nums[j]
            k+=1
            j+=1
        for i in range(len(arr)):
            nums[i+lo]=arr[i]
        return num1+num2+cnt

if __name__ == '__main__':
    sol=Solution()
    nums=[2,4,3,5,1]
    print(sol.reversePairs(nums))
