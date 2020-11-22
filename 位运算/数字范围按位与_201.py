class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        # 找到公共前缀,后面部分补上0

        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift
