from typing import *


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        max1 = self.maxSum(arr)
        mod = int(10 ** 9 + 7)
        sum1 = sum(arr)
        prefix, suffix = 0, 0
        tem_sum = 0
        for val in arr:
            tem_sum += val
            prefix = max(prefix, tem_sum)
        tem_sum = 0
        for val in arr[::-1]:
            tem_sum += val
            suffix = max(suffix, tem_sum)
        if k == 1:
            return max1 % mod
        elif k == 2:
            return max(max1, suffix + prefix) % mod
        else:
            return max(max1, suffix + prefix, suffix + prefix + sum1 * (k - 2)) % mod

    def maxSum(self, arr):
        max_sum = 0
        tem_sum = 0
        for i in range(len(arr)):
            tem_sum += arr[i]
            max_sum = max(max_sum, tem_sum)
            if tem_sum < 0:
                tem_sum = 0
        return max_sum


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 3, -5, 1, 2, 2]
    print(sol.kConcatenationMaxSum(arr, 4))
