import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        因数中只包含2,3,5
        :param n:
        :return:
        """
        list1 = [1]
        set1 = set()
        cnt = 0
        while list1:
            val = heapq.heappop(list1)
            cnt += 1
            if cnt == n:
                return val
            for prime in {2, 3, 5}:
                if val * prime not in set1:
                    heapq.heappush(list1, val * prime)
                    set1.add(val * prime)
        return list1[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.nthUglyNumber(10))
