from typing import *


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        我们需要将一个左边的「较小数」与一个右边的「较大数」交换，
        以能够让当前排列变大，从而得到下一个排列。
        同时我们要让这个「较小数」尽量靠右，而「较大数」尽可能小。
        当交换完成后，「较大数」右边的数需要按照升序重新排列。这样可以在保证新排列大于原来排列的情况下，使变大的幅度尽可能小。
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i - 1 >= 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        idx = i - 1
        j = i
        while j + 1 < len(nums) and nums[j + 1] > nums[idx]:
            j += 1
        nums[idx], nums[j] = nums[j], nums[idx]
        i = idx + 1
        j = len(nums) - 1
        # 注意这步，将后面所有全部逆序排出来
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 3, 1]
    sol.nextPermutation(nums)
    print(nums)
