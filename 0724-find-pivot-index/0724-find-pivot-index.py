class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        left = [0]*n
        right = [0]*n
        l = 0
        for i in range(n):
            left[i] = l
            l += nums[i]
        r = 0
        for i in range(n - 1, -1, -1):
            right[i] = r
            r += nums[i]
        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1
        