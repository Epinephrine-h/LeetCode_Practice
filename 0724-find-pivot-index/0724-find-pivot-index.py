class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        total = sum(nums)
        l = 0
        for i in range(n):
            if l == total - l - nums[i]:
                return i
            l += nums[i]
        return -1
        