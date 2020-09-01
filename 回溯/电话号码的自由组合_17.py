from typing import *


class Solution:

    def __init__(self):
        self.res = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.back(digits, [], 0)
        return self.res

    def back(self, num, list1: List, idx):
        dic1 = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if idx == len(num):
            self.res.append(''.join(list1))
            return
        for i in range(len(dic1[num[idx]])):
            list1.append(dic1[num[idx]][i])
            self.back(num, list1, idx + 1)
            list1.pop()


if __name__ == '__main__':
    sol = Solution()
    digit = '234'
    print(len(sol.letterCombinations(digit)))
