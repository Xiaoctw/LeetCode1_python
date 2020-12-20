from typing import *
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        idxes = {c: i for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')}
        dic1 = defaultdict(lambda: [])
        for str in strs:
            dic1[self.construct_tuple(str,idxes)].append(str)
        res = []
        for str in dic1:
            res.append(dic1[str])
        return res

    def construct_tuple(self, str,idxes):
        list1 = [0] * 26
        for c in str:
            list1[idxes[c]] += 1
        return tuple(list1)


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print(sol.groupAnagrams(strs))
