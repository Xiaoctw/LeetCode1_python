from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        这种题目采用二分搜索时，
        左右两部分一定有一部分是存在顺序的
        :param nums:
        :param target:
        :return:
        '''
        if not nums:
            return -1
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[l]==nums[mid]:#存在重复元素这样解决
                l+=1
                continue
            if nums[l]<nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1


if __name__ == '__main__':
    sol=Solution()
    nums=[1,3,1,1,1]
    print(sol.search(nums,3))

