from typing import *
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        找到两个数组的中位数
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            # 进行一步交换，确保第一个数组比第二个小
            return self.findMedianSortedArrays(nums2,nums1)
        idx_min, idx_max, half_len = 0, m, (m + n + 1) // 2
        while idx_min <= idx_max:
            i = (idx_min + idx_max) // 2
            j = half_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                idx_min = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                idx_max = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return max_of_left
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2