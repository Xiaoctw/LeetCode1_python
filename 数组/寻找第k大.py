# -*- coding:utf-8 -*-

class Solution:
    def findKth(self, a, n, K):
        # write code here
        return self.helper1(a, 0, len(a) - 1, K)

    def helper1(self, nums, lo, hi, K):
        idx = self.helper2(nums, lo, hi)
        if idx - lo + 1 == K:
            return nums[idx]
        if idx - lo + 1 > K:
            return self.helper1(nums, lo, idx - 1, K)
        return self.helper1(nums, idx+1 , hi, K - (idx - lo+1))

    def helper2(self, nums, lo, hi):
        j = lo-1
        val = nums[hi]
        for i in range(lo, hi):
            if nums[i] < val:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[j+1], nums[hi] = nums[hi], nums[j+1]
        return j+1


if __name__ == '__main__':
    sol = Solution()
    nums=[1332802,1177178,1514891,871248,753214,123866,1615405,328656,1540395,968891,1884022,252932,1034406,1455178,821713,486232,860175,1896237,852300,566715,1285209,1845742,883142,259266,520911,1844960,218188,1528217,332380,261485,1111670,16920,1249664,1199799,1959818,1546744,1904944,51047,1176397,190970,48715,349690,673887,1648782,1010556,1165786,937247,986578,798663]
    print(sol.findKth(nums, 49,24))
    nums.sort()
    print(nums[23])
