from typing import *


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        # 求出单个数组可以组成i位的最大数组,利用栈来实现
        def getMaXArr(nums, i):
            if not i:
                return []
            # pop表示最多可以不要nums里几个数字，要不组成不了i位数字
            # 在这里是一个递减的栈，为了保证位数满足要求，栈弹出到一定程度之后
            # 就不再继续弹出
            stack, pop = [], len(nums) - i
            for num in nums:
                while pop and stack and stack[-1] < num:
                    pop -= 1
                    stack.pop()
                stack.append(num)
            # 选择其中前i个数值
            return stack[:i]

        def merge(tmp1, tmp2):
            return [max(tmp1, tmp2).pop(0) for _ in range(k)]

        res = [0] * k
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                # 取num1的i位, num2的k - i
                tmp1 = getMaXArr(nums1, i)
                tmp2 = getMaXArr(nums2, k - i)
                # 合并
                tmp = merge(tmp1, tmp2)
                if res < tmp:
                    res = tmp
        return res
    # 上面一个可以一句话写成

    # return max(merge(getMaXArr(nums1, i), getMaXArr(nums2, k - i)) for i in range(k + 1) if i <= len(nums1) and k -
    # i <= len(nums2))


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 3, 2, 5, 4]
    nums2 = [4, 5, 2, 7, 5]
    print(sol.maxNumber(nums, nums2, 4))
