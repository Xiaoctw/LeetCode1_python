from typing import *
from collections import defaultdict, Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val2cnt = Counter(nums)
        list1 = []
        for val in val2cnt:
            cnt = val2cnt[val]
            if len(list1) < k:
                push(list1, [val, cnt])
            else:
                #说明这个值有可能在最大的K个中，加入到堆里
                if list1[0][1] < cnt:
                    list1[0] = [val, cnt]
                    modify(list1, 0)
        return [val[0] for val in list1]


def modify(list1, idx):
    i = 2 * idx + 1
    j = 2 * idx + 2
    min_idx = idx
    if i < len(list1) and list1[i][1] < list1[min_idx][1]:
        min_idx = i
    if j < len(list1) and list1[j][1] < list1[min_idx][1]:
        min_idx = j
    if min_idx != idx:
        list1[min_idx], list1[idx] = list1[idx], list1[min_idx]
        modify(list1, min_idx)


def push(list1, tup):
    """
    堆插入操作
    :param list1:
    :param tup:
    :return:
    """
    list1.append(tup)
    idx = len(list1) - 1
    while idx > 0:
        idx = (idx - 1) // 2
        modify(list1, idx)


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6, 6]
    print(sol.topKFrequent(nums, 4))
