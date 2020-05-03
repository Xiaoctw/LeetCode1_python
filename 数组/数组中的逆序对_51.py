from typing import List


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0

        # 用于归并的辅助数组
        temp = [0 for _ in range(size)]
        return self.count_reverse_pairs(nums, 0, size - 1, temp)

    def count_reverse_pairs(self, nums, left, right, temp):
        # 在数组 nums 的区间 [left, right] 统计逆序对
        if left == right:
            return 0
        mid = (left + right) >> 1
        #左半部分逆序对
        left_pairs = self.count_reverse_pairs(nums, left, mid, temp)
        #右半部分逆序对
        right_pairs = self.count_reverse_pairs(nums, mid + 1, right, temp)

        reverse_pairs = left_pairs + right_pairs
        # 代码走到这里的时候，[left, mid] 和 [mid + 1, right] 已经完成了排序并且计算好逆序对

        if nums[mid] <= nums[mid + 1]:
            # 此时不用计算横跨两个区间的逆序对，直接返回 reverse_pairs
            return reverse_pairs

        reverse_cross_pairs = self.merge_and_count(nums, left, mid, right, temp)
        return reverse_pairs + reverse_cross_pairs

    def merge_and_count(self, nums, left, mid, right, temp):
        """
        [left, mid] 有序，[mid + 1, right] 有序

        前：[2, 3, 5, 8]，后：[4, 6, 7, 12]
        只在后面数组元素出列的时候，数一数前面这个数组还剩下多少个数字，
        由于"前"数组和"后"数组都有序，
        此时"前"数组剩下的元素个数 mid - i + 1 就是与"后"数组元素出列的这个元素构成的逆序对个数

        """
        for i in range(left, right + 1):
            temp[i] = nums[i]

        i = left
        j = mid + 1
        res = 0
        for k in range(left, right + 1):
            if i > mid:
                nums[k] = temp[j]
                j += 1
            elif j > right:
                nums[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                # 此时前数组元素出列，不统计逆序对
                nums[k] = temp[i]
                i += 1
            else:
                # assert temp[i] > temp[j]
                # 此时后数组元素出列，统计逆序对，快就快在这里，一次可以统计出一个区间的个数的逆序对
                nums[k] = temp[j]
                j += 1
                # 例：[7, 8, 9][4, 6, 9]，4 与 7 以及 7 后面所有的数都构成逆序对
                res += (mid - i + 1)
        return res