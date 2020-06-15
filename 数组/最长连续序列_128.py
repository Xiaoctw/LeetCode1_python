from typing import *
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        max_val=0
        for num in num_set:
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
    nums=[100,4,200,1,3,2]
    print(sol.longestConsecutive(nums))