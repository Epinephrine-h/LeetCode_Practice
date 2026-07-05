class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        right = [0]*n
        r = 0
        for i in range(n - 1, -1, -1):
            right[i] = r
            r += nums[i]
        l = 0
        for i in range(n):
            if l == right[i]:
                return i
            l += nums[i]
        return -1
        