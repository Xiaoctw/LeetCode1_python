from typing import *


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        """
        本题没必要拘束于找到绝对值最小的下标，从头到尾由大到小也是可以的
        :param A:
        :return:
        """
        n = len(A)
        ans = [0] * n

        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if A[i] * A[i] > A[j] * A[j]:
                ans[pos] = A[i] * A[i]
                i += 1
            else:
                ans[pos] = A[j] * A[j]
                j -= 1
            pos -= 1

        return ans



if __name__ == '__main__':
    sol = Solution()
    A = [-11, -10, -8, -4, -1, 0, 3, 10]
    print(sol.sortedSquares(A))
