class TreeArr:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 5)

    def lowbit(self, i):
        return i & (-i)

    def update(self, idx, val):
        while idx <= self.n:
            self.c[idx] += val
            idx += self.lowbit(idx)

    def getSum(self, idx):
        res = 0
        while idx > 0:
            res += self.c[idx]
            idx -= self.lowbit(idx)
        return res


if __name__ == '__main__':
    arr1 = [3, 4, 5, 1, 6, 1, 2, 3, 4, 5, 6, 7]
    arr = TreeArr(len(arr1))
    for i, val in enumerate(arr1):
        arr.update(i + 1, val)
    for i in range(1, len(arr1) + 1):
        print(arr.getSum(i))
    print(sum(arr1))
