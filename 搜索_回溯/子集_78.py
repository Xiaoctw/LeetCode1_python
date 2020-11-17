from typing import *


class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.back([], nums, 0)
        return self.res

    def back(self, tem_list, nums, idx):
        if idx == len(nums):
            self.res.append(tem_list[:])
            return
        self.back(tem_list, nums, idx + 1)
        tem_list.append(nums[idx])
        self.back(tem_list, nums, idx + 1)
        tem_list.pop()


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.subsets(nums))
