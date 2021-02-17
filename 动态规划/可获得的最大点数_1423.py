from typing import *


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        k = n - k
        tem_sum = sum(cardPoints[:k])
        min_val = tem_sum
        for i in range(k, n):
            tem_sum -= cardPoints[i - k]
            tem_sum += cardPoints[i]
            min_val = min(min_val, tem_sum)
        return sum(cardPoints)-min_val


if __name__ == '__main__':
    sol = Solution()
    cardPoints = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    print(sol.maxScore(cardPoints, k))
