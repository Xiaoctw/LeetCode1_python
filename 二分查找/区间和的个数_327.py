from typing import *
import bisect


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # 相当巧妙的方法
        # 首先转化为前缀和，结果res每次添加的都是
        # 以当前元素为最后一个元素的集合有多少个
        # 主需要在之前的那么多个前缀和中找到在tem_sum-upper和tem_sum-lower中的就可以
        # 已经处理过的前缀和需要排好序
        pre = [0]  # 前缀和，填一个0
        res, tem_sum = 0, 0
        for val in nums:
            tem_sum += val
            res += bisect.bisect_right(pre, tem_sum - lower) - bisect.bisect_left(pre, tem_sum - upper)
            bisect.insort(pre, tem_sum)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    lower = 5
    upper = 10
    sol = Solution()
    print(sol.countRangeSum(nums, lower, upper))
