from typing import *
from collections import defaultdict


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        first = {}
        last = {}
        for i, c in enumerate(S):
            if c not in first:
                first[c] = i
                last[c] = i
            else:
                last[c] = i
        list1 = []
        for c in first:
            list1.append((first[c], last[c]))
        list1.sort()
        idx_es = [0]
        last = list1[0][1]
        j=0
        while j<len(list1):
            if list1[j][0]<=last:
                last=max(last,list1[j][1])
            else:
                idx_es.append(list1[j][0])
                last=list1[j][1]
            j+=1
        idx_es.append(len(S))
        res = []
        for i in range(1, len(idx_es)):
            res.append(idx_es[i] - idx_es[i - 1])
        return res


if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    sol = Solution()
    print(sol.partitionLabels(s))
