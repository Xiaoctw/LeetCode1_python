from typing import *


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_val, min_val = max(nums), min(nums)
        if min_val == max_val:
            return 0
        # 确保bucket的长度至少为1
        len_bucket = max(1, (max_val - min_val) // (len(nums) - 1))
        num_bucket = (max_val - min_val) // len_bucket + 1
        buckets = [[float('inf'), -float('inf')] for _ in range(num_bucket)]
        # bucket中只存放最大值最小值就行
        for val in nums:
            idx = (val - min_val) // len_bucket
            buckets[idx][0] = min(buckets[idx][0], val)
            buckets[idx][1] = max(buckets[idx][1], val)
        pre_max = None
        max_gap = 0
        for i in range(num_bucket):
            if buckets[i][0] != float('inf') and pre_max:
                max_gap = max(max_gap, buckets[i][0] - pre_max)
            if buckets[i][0] != float('inf'):
                pre_max = buckets[i][1]
        return max_gap


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 1, 1, 5, 5, 5, 5, 5]
    print(sol.maximumGap(nums))
