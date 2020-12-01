from typing import *
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        max_val=nums[1]-nums[0]
        for i in range(2,len(nums)):
            max_val=max(max_val,nums[i]-nums[i-1])
        return max_val

if __name__ == '__main__':
    sol=Solution()
    nums=[3,6,9,1]
    print(sol.maximumGap(nums))