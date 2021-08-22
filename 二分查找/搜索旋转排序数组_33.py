from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[0]: #这里可能相等
                if nums[0]<=target<nums[mid]:
                    hi=mid-1
                else:
                    lo=mid+1
            else:
                if nums[mid]<target<=nums[len(nums)-1]:
                    lo=mid+1
                else:
                    hi=mid-1
        return -1

if __name__ == '__main__':
    nums=[3,1]
    sol=Solution()
    print(sol.search(nums,1))