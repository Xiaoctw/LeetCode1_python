from typing import *
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1={}
        stack=[]
        for val in nums2:
            while stack and stack[-1]<val:
                map1[stack[-1]]=val
                stack.pop()
            stack.append(val)
        for val in stack:
            map1[val]=-1
        res=[]
        for val in nums1:
            res.append(map1[val])
        return res

if __name__ == '__main__':
    sol=Solution()
    nums1=[4,1,2]
    num2=[1,3,4,2]
    print(sol.nextGreaterElement(nums1,num2))