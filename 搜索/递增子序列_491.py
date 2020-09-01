from typing import *
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, [], 0)
        return self.res

    def helper(self, nums, temp, idx):
        if idx == len(nums):
            if len(temp) >= 2:
                self.res.append(temp[:])
            return
        if not temp or nums[idx] >= temp[-1]:
            temp.append(nums[idx])
            self.helper(nums, temp, idx + 1)
            temp.pop()
        # 这一步是去重，如果说该位置的元素和末尾元素相同，不能不加入，就调用
        if idx > 0 and temp and nums[idx] == temp[-1]:
            return
        self.helper(nums, temp, idx + 1)


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 4, 6, 7, 7, 3, 2, 1]
    list1 = sol.findSubsequences(nums)
    for l in list1:
        print(l)
