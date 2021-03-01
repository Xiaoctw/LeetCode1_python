from typing import *


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        sums1, sums2 = [0] * (n + 1), [0] * (n + 1)
        for i in range(1, n + 1):
            sums1[i] = sums1[i - 1] + customers[i - 1]
            if grumpy[i - 1] == 1:
                sums2[i] = sums2[i - 1]
            else:
                sums2[i] = sums2[i - 1] + customers[i - 1]
        max_val = 0
        for i in range(1, n + 2 - X):
            tem_val = sums1[i + X - 1] - sums1[i - 1]
            tem_val += sums2[i - 1]
            tem_val += sums2[-1] - sums2[i + X - 1]
            max_val = max(tem_val, max_val)
        return max_val


if __name__ == '__main__':
    sol = Solution()
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    print(sol.maxSatisfied(customers, grumpy, X))
