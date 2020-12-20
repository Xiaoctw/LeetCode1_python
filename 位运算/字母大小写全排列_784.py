from typing import *


class Solution:
    def __init__(self):
        self.ans = []
        s1 = 'abcdefghijklmnopqrstuvwxyz'
        s2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.dic1 = {}
        for i in range(len(s2)):
            self.dic1[s2[i]] = s1[i]
            self.dic1[s1[i]] = s2[i]

    def letterCasePermutation(self, S: str) -> List[str]:
        self.back(S, [], 0)
        return self.ans

    def back(self, S, tem_res, idx):
        if idx >= len(S):
            self.ans.append(''.join(tem_res[:]))
            return
        if S[idx] not in self.dic1:
            tem_res.append(S[idx])
            self.back(S, tem_res, idx + 1)
            tem_res.pop()
        else:
            tem_res.append(S[idx])
            self.back(S, tem_res, idx + 1)
            tem_res.pop()
            tem_res.append(self.dic1[S[idx]])
            self.back(S, tem_res, idx + 1)
            tem_res.pop()


if __name__ == '__main__':
    sol = Solution()
    S = "a1b2"
    print(sol.letterCasePermutation(S))
