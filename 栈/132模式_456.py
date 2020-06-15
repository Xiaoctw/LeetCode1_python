from typing import *
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        stack=[]
        arr=[0]*len(nums)
        arr[0]=nums[0]
        for i in range(len(nums)):
            arr[i]=min(nums[i],arr[i-1])
        for j in range(len(nums)-1,-1,-1):
            if nums[j]>arr[j]:
                while stack and stack[-1]<=arr[j]:
                    stack.pop()
                if stack and stack[-1]<nums[j]:
                    return True
                stack.append(nums[j])
        return False
if __name__ == '__main__':
    sol=Solution()
    print(sol.find132pattern([3,1,4,4,2]))