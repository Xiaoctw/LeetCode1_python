from typing import *


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        list1 = list('abcdefghijklmnopqrstuvwxyz')
        dic1 = {c: i for i, c in enumerate(list1)}
        lo, hi = 0, len(letters) - 1
        letters.sort(key=lambda x: dic1[x])
        idx = lo
        while lo <= hi:
            mid = (lo + hi) // 2
            if dic1[letters[mid]] <= dic1[target]:
                lo = mid + 1
            else:
                hi = mid - 1
        if lo == len(letters):
            return letters[0]
        return letters[lo]


if __name__ == '__main__':
    sol = Solution()
    letters = ['c', 'f', 'j']
    target = 'h'
    print(sol.nextGreatestLetter(letters, target))
