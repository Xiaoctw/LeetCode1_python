from typing import *
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        max_val=0
        for num in num_set:
            #这个判断保证每个数字都只遍历到一次，复杂度不会过高
            if num-1 not in num_set:
                current_num=num
                len1=1
                while current_num+1 in num_set:
                    current_num+=1
                    len1+=1
                max_val=max(max_val,len1)
        return max_val

if __name__ == '__main__':
    sol=Solution()
    nums=[100,4,200,1,3,2,0,6,5,7,8,9,10,13,12,11]
    print(sol.longestConsecutive(nums))