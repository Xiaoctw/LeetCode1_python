from typing import *


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        res = None
        for i in range(min(len(nums1), k) + 1):
            list1 = self.helper(nums1, i)
            list2 = self.helper(nums2, k - i)
            if len(list1) + len(list2) < k:
                continue
            list3 = self.merge(list1, list2, k)
            if not res or res < list3:
                res = list3
        return res

    def helper(self, nums, k):
        stack = []
        max_pop = len(nums) - k
        pop_num = 0
        for num in nums:
            while stack and stack[-1] < num and pop_num < max_pop:
                stack.pop()
                pop_num += 1
            stack.append(num)
        return stack[:k]

    def merge(self, nums1, nums2, k):
        return [max(nums1, nums2).pop(0) for _ in range(k)]


if __name__ == '__main__':
    sol = Solution()
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    print(sol.maxNumber(nums1, nums2, k))
