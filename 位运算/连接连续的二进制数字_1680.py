from typing import *


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        shift = -1
        mod = 10 ** 9 + 7
        for i in range(n + 1):
            # 判断是否为2的幂次
            if i & (i - 1) == 0:
                shift += 1
            ans = ((ans << shift) + i) % mod
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 12
    print(sol.concatenatedBinary(n))
