from typing import *


class TreeArr:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n + 4)

    def lowbit(self, i):
        return i & (-i)

    def update(self, idx, val):
        while idx <= self.n:
            self.arr[idx] += val
            idx += self.lowbit(idx)

    def get_sum(self, idx):
        res = 0
        while idx > 0:
            res += self.arr[idx]
            idx -= self.lowbit(idx)
        return res


class Solution:
    """
    对于每个下标 j，以 j 为右端点的下标对的数量，
    就等于数组 preSum[0..j-1] 中的所有整数，出现在区间 [preSum[j]-upper,preSum[j]-lower] 的次数
    """
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        value2idx={}
        pre_Sum=[0]
        for val in nums:
            pre_Sum.append(pre_Sum[-1]+val)
        set1=set()
        for val in pre_Sum:
            set1.add(val)
            set1.add(val-lower)
            set1.add(val-upper)
        list1=list(set1)
        list1.sort()
        cnt=1
        for val in list1:
            value2idx[val]=cnt
            cnt+=1
        treeArr = TreeArr(cnt)
        res = 0
        for val in pre_Sum:
            left, right = value2idx[val - upper], value2idx[val - lower]
            res += (treeArr.get_sum(right) - treeArr.get_sum(left-1))
            treeArr.update(value2idx[val], 1)

        return res

if __name__ == '__main__':
    sol=Solution()
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    print(sol.countRangeSum(nums,lower,upper))

