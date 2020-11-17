from typing import *


class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.dfs([], nums, 0)
        return self.res

    def dfs(self, tem_list, nums, idx):
        if idx == len(nums) - 1:
            list1 = tem_list[:]
            list1.append(nums[idx])
            self.res.append(list1)
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            tem_list.append(nums[idx])
            self.dfs(tem_list, nums, idx + 1)
            tem_list.pop()
            nums[idx], nums[i] = nums[i], nums[idx]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4]
    print(sol.permute(nums))
