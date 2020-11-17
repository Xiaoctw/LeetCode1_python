from typing import *


class Solution:
    """
    每次找到最大的因数，然后想办法得到它，在复制多次得到最终结果。
    """

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        for i in range(n // 2, 0, -1):
            if n % i == 0:
                return self.minSteps(i) + n // i
        return n


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSteps(30))
