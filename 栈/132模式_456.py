from typing import *
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        max_top=-float('inf')
        stack=[nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<max_top:
                return True
            while stack and stack[-1]<nums[i]:
                max_top=max(max_top,nums[i])
                stack.pop()
            stack.append(nums[i])
        return False




if __name__ == '__main__':
    sol=Solution()
    print(sol.find132pattern([3,5,0,3,4]))