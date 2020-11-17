import random


class QuickSort:
    def partition(self, nums, i, j):
        p0, p1 = i, i
        idx1 = random.randint(i, j)
        idx2 = random.randint(i, j)
        val1, val2 = min(nums[idx1], nums[idx2]), max(nums[idx1], nums[idx2])
        for k in range(i, j + 1):
            if nums[k] <= val1:
                nums[k], nums[p0] = nums[p0], nums[k]
                if p0 < p1:
                    nums[p1], nums[k] = nums[k], nums[p1]
                p1 += 1
                p0 += 1
            elif val1 < nums[k] < val2:
                nums[k], nums[p1] = nums[p1], nums[k]
                p1 += 1
        return p0, p1

    def sort(self, nums, i, j):
        if i >= j:
            return
        p0, p1 = self.partition(nums, i, j)
        self.sort(nums, i, p0 - 1)
        self.sort(nums, p0, p1 - 1)
        self.sort(nums, p1, j)


if __name__ == '__main__':
    quick_sort = QuickSort()
    nums = [4, 3, 5, 2, 6, 2, 6, 3, 1, 6, 8, 4, 2, 5, 7, 8]
    quick_sort.sort(nums, 0, len(nums) - 1)
    print(nums)
