from typing import *


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        本题和图无关，是一个动态规划的题目
        首先排序，排序的指标为年龄大的在后面，
        这样就可以在比起年龄小的人中找到合适的人了。
        dp[i]为最后一位为i时可以获得最大score，
        :param scores:
        :param ages:
        :return:
        """
        list1 = []
        for i in range(len(scores)):
            list1.append((ages[i], scores[i]))
        list1.sort()
        dp = [0] * len(scores)
        dp[0] = list1[0][1]
        for i in range(1, len(list1)):
            dp[i] = list1[i][1]
            for j in range(i):
                if list1[j][1] <= list1[i][1]:
                    dp[i] = max(dp[i], dp[j] + list1[i][1])
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    scores = [1,2,3,5]
    ages = [8,9,10,1]
    print(sol.bestTeamScore(scores, ages))
