from typing import *
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        list1=nums[:]
        return self.solve(list1)

    def solve(self,nums):
        if len(nums)==0:
            return False
        if len(nums)==1:
            return abs(nums[0]-24)<=1e-5
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    list1=[nums[k] for k in range(len(nums)) if k!=i and k!=j]
                    for ope in ['+','-','*','/']:
                        if ope=='+':
                            list1.append(nums[i]+nums[j])
                        elif ope=='-':
                            list1.append(nums[i]-nums[j])
                        elif ope=='*':
                            list1.append(nums[i]*nums[j])
                        else:
                            if nums[j]==0:
                                continue
                            list1.append(nums[i]/nums[j])
                        if self.solve(list1):
                            return True
                        list1.pop()
        return False

if __name__ == '__main__':
    sol=Solution()
    print(sol.judgePoint24([1,3,2,6]))