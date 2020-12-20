class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        num_list = []
        while N:
            num_list.append(N % 10)
            N //= 10
        num_list.reverse()
        pre_val = num_list[-1]
        has_less = [False] * len(num_list)
        for i in range(len(num_list) - 1, -1, -1):
            if num_list[i] > pre_val:
                has_less[i] = True
                pre_val = num_list[i] - 1
            pre_val = min(pre_val, num_list[i])
        res = []
        flag = False
        for i in range(len(num_list)):
            if flag:
                res.append(9)
                continue
            if not has_less[i]:
                res.append(num_list[i])
            else:
                res.append(num_list[i] - 1)
                flag = True
        ans = 0
        for val in res:
            ans = ans * 10 + val
        return ans


if __name__ == '__main__':
    sol = Solution()
    N = 120
    print(sol.monotoneIncreasingDigits(N))
