from typing import *


class Solution:
    def __init__(self):
        self.ans=[]
    def splitIntoFibonacci(self, S: str) -> List[int]:
        self.backtrack(S,0)
        return self.ans


    def backtrack(self,S,index):
        if index == len(S):
            return len(self.ans) >= 3
        curr = 0
        for i in range(index, len(S)):
            if i > index and S[index] == "0":
                break
            curr = curr * 10 + ord(S[i]) - ord("0")
            if curr > 2 ** 31 - 1:
                break

            if len(self.ans) < 2 or curr == self.ans[-2] + self.ans[-1]:
                self.ans.append(curr)
                if self.backtrack(S,i + 1):
                    return True
                self.ans.pop()
            elif len(self.ans) > 2 and curr > self.ans[-2] + self.ans[-1]:
                break
        return False


if __name__ == '__main__':
    S = '112358130'
    sol = Solution()
    print(sol.splitIntoFibonacci(S))
