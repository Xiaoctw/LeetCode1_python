from typing import *
from collections import defaultdict


class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = {}
        max_val = 1
        for val in arr:
            if val - difference in dic:
                dic[val] = dic[val - difference] + 1
            else:
                dic[val] = 1
            max_val = max(max_val, dic[val])
        return max_val


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff = -2
    print(sol.longestSubsequence(arr, diff))
