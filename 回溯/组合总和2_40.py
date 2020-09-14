from typing import *
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx: int, rest: int):
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:])
                return
            if idx == len(freq) or rest < freq[idx][0]:
                return
            dfs(idx + 1, rest)

            # 最多可选的个数
            most = min(rest // freq[idx][0], freq[idx][1])
            for i in range(1, most + 1):
                sequence.append(freq[idx][0])
                dfs(idx + 1, rest - i * freq[idx][0])
            sequence = sequence[:-most]

        freq = sorted(Counter(candidates).items())
        ans, sequence = [], []
        dfs(0, target)
        return ans


if __name__ == '__main__':
    list1 = [2, 5, 2, 1, 2]
    target = 5
    sol = Solution()
    print(sol.combinationSum2(list1, target))
