from typing import *
class Solution:
    '''
    减少空间复杂度的方法为将pro_left数组作为输出数组，
    动态规划构造pro_left数组过程中，利用常数实现
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len1=len(nums)
        res=[0]*len1
        res[0]=1
        for i in range(1,len1):
            res[i]=res[i-1]*nums[i-1]
        r=1
        for i in range(len1-1,-1,-1):
            res[i]=res[i]*r
            r*=nums[i]
        return res

if __name__ == '__main__':
    sol=Solution()
    nums1=[1,2,3,4,5,6,5]
    print(sol.productExceptSelf(nums1))