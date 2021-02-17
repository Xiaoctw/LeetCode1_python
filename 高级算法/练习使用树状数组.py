class TreeArr:
    def __init__(self, n):
        self.n = n
        # 树状数组0号下表不为0，lowbit运算不支持0
        # 下标从1开始
        self.c = [0] * (n + 5)

    # 找到某个数最低二进制位所对应的值
    def lowbit(self, i):
        return i & (-i)

    def update(self, idx, val):
        """
        在idx下表处加上val值,
        在某个位置加上某个数后，对后面会有影响，
        因此需要不断递增
        :param idx:
        :param val:
        :return:
        """
        while idx <= self.n:
            self.c[idx] += val
            idx += self.lowbit(idx)

    def getSum(self, idx):
        """
        求idx之前元素和，
        需要像前面找元素
        :param idx:
        :return:
        """
        res = 0
        while idx > 0:
            res += self.c[idx]
            idx -= self.lowbit(idx)
        return res


if __name__ == '__main__':
    arr1 = [3, 4, 5, 1, 6, 1, 2, 3, 4, 5, 6, 7]
    arr = TreeArr(len(arr1))
    for i, val in enumerate(arr1):
        # 某个下标出加上某个值
        arr.update(i + 1, val)
    for i in range(1, len(arr1) + 1):
        print(arr.getSum(i))
    print(sum(arr1))
