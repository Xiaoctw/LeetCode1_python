from typing import *


class Solution:
    def __init__(self):
        self.res = []
        self.visited = None

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        #通过判断是否访问过来达到去重的目的
        self.visited = [False] * n
        self.dfs([], nums)
        return self.res

    def dfs(self, tem_list, nums):
        if len(tem_list) == len(nums):
            self.res.append(tem_list[:])
            return
        for i in range(0, len(nums)):
            # 在这里选择可以添加的元素是什么
            if self.visited[i] or (i>0 and nums[i] == nums[i - 1] and not self.visited[i - 1]):
                continue
            tem_list.append(nums[i])
            self.visited[i] = True
            self.dfs(tem_list, nums)
            self.visited[i] = False
            tem_list.pop()


if __name__ == '__main__':
    sol = Solution()
    nums = [1]
    print(sol.permuteUnique(nums))
