from typing import *


class Solution:
    def __init__(self):
        self.res = []
        self.visited = None

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.visited = [False] * len(candidates)
        candidates.sort()
        self.back(candidates, [], 0, target)
        return self.res

    def back(self, candidates, tem_list, tem_sum, target):
        if tem_sum == target:
            self.res.append(tem_list[:])
            return
        for i in range(len(candidates)):
            # 选择一个要添加的元素
            # 这里需要注意，相同元素必须在前一个已经访问的前提下才能访问该元素，就可以去重
            if self.visited[i] or tem_sum + candidates[i] > target or (
                    i > 0 and candidates[i] == candidates[i - 1] and not self.visited[i - 1]) or (
                    len(tem_list) > 0 and candidates[i] < tem_list[-1]):
                continue
            tem_list.append(candidates[i])
            self.visited[i] = True
            self.back(candidates, tem_list, tem_sum + candidates[i], target)
            self.visited[i] = False
            tem_list.pop()


if __name__ == '__main__':
    list1 = [2, 5, 2, 1, 2]
    target = 5
    sol = Solution()
    print(sol.combinationSum2(list1, target))
