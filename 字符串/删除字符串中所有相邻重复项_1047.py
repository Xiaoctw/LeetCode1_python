class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if not stack:
                stack.append(c)
            else:
                if stack[-1] == c:
                    stack.pop()
                else:
                    stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':
    sol = Solution()
    s = 'abbaca'
    print(sol.removeDuplicates(s))
