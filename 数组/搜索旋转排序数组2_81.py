from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        beg,end=0,len(nums)-1
        while beg<=end:
            mid=(beg+end)//2
            if nums[mid]==target:#这一步很重要
                return True
            if nums[beg]==nums[mid]:
                beg+=1
                continue
            if nums[beg]<nums[mid]:
            #前半部分有序
                if nums[beg]<=target<nums[mid]:
                    end=mid-1
                else:
                    beg=mid+1
            else:
                if nums[mid]<target<=nums[end]:
                    beg+=1
                else:
                    end-=1
        return False


if __name__ == '__main__':
    sol=Solution()
    nums=[1,3,1,1,1]
    print(sol.search(nums,3))