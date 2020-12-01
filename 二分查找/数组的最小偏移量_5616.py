from typing import *
import bisect


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        list1 = []
        for val in nums:
            if val & 1:
                # list1.append(val*2)
                bisect.insort_left(list1, val * 2)
            else:
                # list1.append(val)
                bisect.insort_left(list1, val)
        res = list1[-1] - list1[0]
        while res > 0 and not list1[-1] & 1:
            res = min(res, list1[-1] - list1[0])
            val = list1[-1]
            list1.pop()
            bisect.insort_left(list1, val // 2)
        res = min(res, list1[-1] - list1[0])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    sol = Solution()
    print(sol.minimumDeviation(nums))
