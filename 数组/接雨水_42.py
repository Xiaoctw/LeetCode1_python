from typing import *
import sys


class Solution:
    """
    接雨水
    """
    def trap(self, height: List[int]) -> int:
        '''
        分别找到某个柱左边最高和右边最高
        :param height:
        :return:
        '''
        _len = len(height)
        max_left, max_right = [0] * _len, [0] * _len
        max_val = -sys.maxsize
        for i, val in enumerate(height):
            max_val = max(max_val, val)
            max_left[i] = max_val
        max_val = -sys.maxsize
        for i in range(_len - 1, -1, -1):
            max_val = max(max_val, height[i])
            max_right[i] = max_val
        res = 0
        for i in range(_len):
            res += min(max_left[i], max_right[i]) - height[i]
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(sol.trap(nums))
