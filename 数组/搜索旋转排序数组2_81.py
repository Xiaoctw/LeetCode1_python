from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:#这步很重要
                return True
            if nums[l]==nums[mid]: #这里排除了l位置为待查找元素情况
                l+=1
                continue
            if nums[l]<nums[mid]:#前半部分有序
                if nums[l]<=target<=nums[mid]:
                    r=mid-1#mid位置肯定不是，之前已经查看过了
                else:
                    l=mid+1
            else:
                if nums[mid]<=target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return False


if __name__ == '__main__':
    sol=Solution()
    nums=[1,1,1,1,1,3,1,1,1]
    print(sol.search(nums,3))