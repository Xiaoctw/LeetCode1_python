from typing import *


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        max_depth = 0
        stack = []
        for c in seq:
            if c == '(':
                stack.append(c)
                max_depth = max(max_depth, len(stack))
            else:
                stack.pop()
        max_depth = max_depth // 2
        ans = []
        cnt = 0
        for c in seq:
            if c == '(':
                if cnt < max_depth:
                    ans.append(0)
                    cnt += 1
                else:
                    ans.append(1)
            else:
                if cnt > 0:
                    cnt -= 1
                    ans.append(0)
                else:
                    ans.append(1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    seq = "()(())()"
    print(sol.maxDepthAfterSplit(seq))
