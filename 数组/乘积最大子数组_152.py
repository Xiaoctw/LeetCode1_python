from typing import *
import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        max_val=-sys.maxsize
        tem_max,tem_min=1,1#以当前值为结尾的数组的最大和
        for val in nums:
            a, b = tem_max, tem_min
            if val>0:
                tem_max=max(val,val*a)
                tem_min=min(val,val*b)
            elif val<0:
                tem_max = max(val, val * b)
                tem_min = min(val, val * a)
            else:
                tem_max,tem_min=0,0
            max_val=max(tem_max,max_val)
        return max_val

if __name__ == '__main__':
    sol=Solution()
    nums=[-2,0,-1,3,-3,-4]
    s='this is a blue'
    print(sol.maxProduct(nums))
    print(list(reversed(s.split())))
