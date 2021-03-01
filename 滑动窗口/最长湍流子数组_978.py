from typing import *


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        r = 1
        l = 0
        max_len = 1
        # if len(arr)==2 and arr[0]==arr[1]:
        #     return 1
        while r < len(arr):
            if arr[r] == arr[r - 1]:
                l = r
            elif r == 1 or (arr[r] - arr[r - 1]) * (arr[r - 1] - arr[r - 2]) < 0:
                max_len = max(max_len, r - l + 1)
            else:
                l = r - 1
            r += 1
        return max_len


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 1]
    print(sol.maxTurbulenceSize(arr))
