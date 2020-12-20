from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnts = defaultdict(lambda: 0)
        for c in s:
            cnts[c] += 1
        stack = []
        set1 = set()
        for c in s:
            # 注意这里，如果当前字符已经在栈中就不要在和栈顶元素比较了
            if c not in set1:
                while stack and ord(stack[-1]) >= ord(c) and cnts[stack[-1]] >= 1:
                    set1.remove(stack[-1])
                    stack.pop()
                stack.append(c)
                set1.add(c)
                cnts[c] -= 1
            else:
                cnts[c] -= 1
        return ''.join(stack)


if __name__ == '__main__':
    sol = Solution()
    s = "cbacdcbc"
    print(sol.removeDuplicateLetters(s))
