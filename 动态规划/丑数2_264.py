class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0
        arr = [1]
        for j in range(1, n):
            val = min(arr[i2] * 2, arr[i3] * 3, arr[i5] * 5)
            arr.append(val)
            if val == arr[i2] * 2:
                i2 += 1
            if val == arr[i3] * 3:
                i3 += 1
            if val == arr[i5] * 5:
                i5 += 1
        return arr[n - 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.nthUglyNumber(10))
