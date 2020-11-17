from typing import *


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0,p2=0,len(nums)-1
        i=0
        while i<p2:
            if nums[i]==0:
                nums[p0],nums[i]=nums[i],nums[p0]
                p0+=1
            elif nums[i]==2:
                nums[i],nums[p2]=nums[p2],nums[i]
                p2-=1
            i+=1


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 0, 1, 1, 2, 0, 1, 1, 2]
    sol.sortColors(nums)
    print(nums)
