from typing import *


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        '''
        本题dp代表的含义比较特殊，含义为从i-j，当前玩家比另一个玩家最多多多少
        因为每次进行操作的玩家不同，但是不同玩家最终目的都是相同的
        :param piles:
        :return:
        '''
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.stoneGame([5, 3, 4, 5]))
