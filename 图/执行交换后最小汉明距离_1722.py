from typing import *
from collections import defaultdict

class Solution:
    def __init__(self):
        self.arr = None

    def minimumHammingDistance(self, source: List[int],
                               target: List[int], allowedSwaps: List[List[int]]) -> int:
        len1 = len(source)
        self.arr = [i for i in range(len1)]
        for swap in allowedSwaps:
            self.set_union(swap[0], swap[1])
        head2src = defaultdict(lambda: [])
        head2tar = defaultdict(lambda: [])
        head2set = defaultdict(lambda: set())
        for i in range(len1):
            head2src[self.find(i)].append(source[i])
            head2tar[self.find(i)].append(target[i])
            head2set[self.find(i)].add(source[i])
            head2set[self.find(i)].add(target[i])
        res = 0
        for head in head2set:
            res += self.cnt(head2src[head], head2tar[head], head2set[head])
        return res

    def cnt(self, list1, list2, set1):
        res = 0
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        for val in list1:
            dic1[val] += 1
        for val in list2:
            dic2[val] += 1
        for val in set1:
            res += abs(dic1[val] - dic2[val])
        return res//2

    def set_union(self, i, j):
        find_j = self.find(j)
        find_i = self.find(i)
        if find_i != find_j:
            self.arr[find_i] = find_j

    def find(self, i):
        if i != self.arr[i]:
            self.arr[i] = self.find(self.arr[i])
        return self.arr[i]


if __name__ == '__main__':
    sol = Solution()
    source = [1,2,3,4]
    target = [1,3,2,4]
    allowedSwaps = []
    print(sol.minimumHammingDistance(source,target,allowedSwaps))
