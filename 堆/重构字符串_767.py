import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S
        c2cnt = Counter(S)
        que = [(-c2cnt[c], c) for c in c2cnt]
        # 维护一个堆
        heapq.heapify(que)
        res = ''
        while len(que) >= 2:
            cnt1, c1 = heapq.heappop(que)
            cnt2, c2 = heapq.heappop(que)
            if not res:
                res = c1 + c2
            elif res[-1] == c1:
                res += (c2 + c1)
            else:
                res += (c1 + c2)
            if -cnt1 > 1:
                heapq.heappush(que, (cnt1 + 1, c1))
            if -cnt2 > 1:
                heapq.heappush(que, (cnt2 + 1, c2))
        if len(que) == 1:
            if -que[0][0] > 1:
                return ''
            res += que[0][1]
        return res


if __name__ == '__main__':
    sol = Solution()
    s="abbabbaaab"
    print(sol.reorganizeString(s))
