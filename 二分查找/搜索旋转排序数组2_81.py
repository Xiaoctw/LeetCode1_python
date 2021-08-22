from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if target in {nums[mid],nums[lo],nums[hi]}:
                return True
            if nums[lo]==nums[hi]:
                lo+=1 #在减掉1的之前，要看一看这个位置是否符合要求。
                continue

            if nums[mid]>=nums[0]:
                if nums[lo]<=target<nums[mid]:
                    hi=mid-1
                else:
                    lo=mid+1

            else:
                if nums[mid]<target<=nums[len(nums)-1]:
                    lo=mid+1
                else:
                    hi=mid-1
        return False

if __name__ == '__main__':
    nums=[1,13,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    sol=Solution()
    print(sol.search(nums,13))