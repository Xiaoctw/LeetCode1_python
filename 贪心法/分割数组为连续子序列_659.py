from typing import *
from collections import defaultdict


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        dic = defaultdict(lambda: [])
        for num in nums:
            if num - 1 not in dic or len(dic[num - 1]) == 0:
                dic[num].append([num])
            else:
                list1 = None
                for l in dic[num - 1]:
                    if list1 is None or len(l) < len(list1):
                        list1 = l
                dic[num - 1].remove(list1)
                list1.append(num)
                dic[num].append(list1)
        for num in dic:
            for l in dic[num]:
                if len(l) < 3:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 4, 5]
    print(sol.isPossible(nums))
